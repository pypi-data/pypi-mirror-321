from .logger import Logger
from .constants import *
from .responses import *
from typing import List
import requests
import aiohttp
import asyncio
import random
import time
import json
import re

logger = Logger()

class InitializationError(Exception):
    pass

def extrct_gs_shapshot_time(url):
    match = re.search(r'_(\d+)\.json$', url)
    if match:
        return int(match.group(1))
    else:
        return None

def validate_order(order, input_type="create", idx=0):
    price = order.get("price")
    oc = order.get("oc")
    allowed_oc_keys = ["pl", "core_lock", "mem_lock", "mem_offset", "core_offset"]

    if oc:
        if not isinstance(oc, list):
            logger.error(f"create_orders | #{str(idx)} | invalid oc input")
            return False
        if len(oc) == 0:
            logger.error(f"create_orders | #{str(idx)} | invalid oc input")
            return False
        for this_gpu_oc in oc:
            pl = this_gpu_oc.get("pl")
            oc_keys = this_gpu_oc.keys()
            if not pl:
                logger.error(f"create_orders | #{str(idx)} | invalid oc input | PL must be specified!")
                return False
            for key in oc_keys:
                if not key in allowed_oc_keys:
                    logger.error(f"create_orders | #{str(idx)} | invalid oc input | key {key} does not fit specification")
                    return False
                if not isinstance(this_gpu_oc[key], int):
                    logger.error(f"create_orders | #{str(idx)} | invalid oc input | key {key} value must be int")
                    return False

    if input_type=="create":
        renting_server = order.get("renting_server")
        env = order.get("env")
        if not price or not isinstance(price, (int, float)) or price < 0.0001 or price > 5000:
            logger.error(f"create_orders | #{str(idx)} | invalid price input")
            return False
        if not renting_server or not isinstance(renting_server, int):
            logger.error(f"create_orders | #{str(idx)} | invalid server_id input")
            return False
        if not oc:
            logger.error(f"create_orders | #{str(idx)} | oc input is mandatory")
            return False
        if env and type(env) != dict:
            logger.error(f"create_orders | #{str(idx)} | env must be dict")
            return False
        if env:
            env_keys = env.keys()
            env_str = json.dumps(env)
            if len(env_str) >= 12288:
                logger.error(f"create_orders | #{str(idx)} | stringified ENV length must be under 12288 characters")
                return False
            for key in env_keys:
                if len(key) > 128:
                    logger.error(f"create_orders | #{str(idx)} | ENV variable name must be up to 128 characters")
                    return False
                elif len(env[key]) > 1536:
                    logger.error(f"create_orders | #{str(idx)} | ENV variable value must be up to 1536 characters")
                    return False

    elif input_type=="edit":
        order_id = order.get("order_id")
        if not price or not isinstance(price, (int, float)) or price < 0.0001 or price > 5000:
            logger.error(f"edit_orders | #{str(idx)} | invalid order_id")
            return False
        if not order_id or not isinstance(order_id, int):
            logger.error(f"edit_orders | #{str(idx)} | invalid order_id")
            return False

    return True
        

class gigaspot_connection:
    def __init__(self, gigaspot_api_key):
        self.gigaspot_api_key = gigaspot_api_key
        self.my_user_id = None
        self.last_v1_snapshot_url = ''
        self.last_v1_snapshot = {}
        self.last_clore_price = 0

        for i in range(0,3):
            data = None
            try:
                response = requests.get(CLORE_API+"/v1/get_gigaspot", headers=self.generate_headers(), timeout=20)
                data=response.json()
            except Exception as e:
                pass
            if type(data) != dict:
                pass
            elif "my_user_id" in data:
                logger.log("Connected to CLORE.AI")
                self.my_user_id = data["my_user_id"]
                return
            elif "code" in data and data["code"] == 3:
                logger.error("Invalid CLORE.AI API token")
            time.sleep(5)
        logger.error("Could not connect to clore.ai")
    
    def generate_headers(self, base={}):
        if type(base) != dict:
            base = {}
        base["Content-Type"] = "application/json"
        base["auth"] = self.gigaspot_api_key
        return base

    async def get_gigaspot(self, retries=3):
        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(
                        CLORE_API + "/v1/get_gigaspot",
                        headers=self.generate_headers(),
                        timeout=20,
                    ) as clore_res:
                        if clore_res.status == 429:
                            retry_after = clore_res.headers.get("Retry-After")
                            if retry_after:
                                delay = int(retry_after)  # Respect server's Retry-After header
                            else:
                                delay = random.uniform(2, 5)  # Fallback random delay
                            logger.error(f"get_gigaspot | HTTP 429 received. Retrying after {delay:.2f} seconds...")
                            await asyncio.sleep(delay)
                            continue  # Retry the request
                        elif clore_res.status == 200:
                            data = await clore_res.json()
                            if "v1_snapshot_url" in data:
                                if not self.my_user_id:
                                    self.my_user_id = data["my_user_id"]
                                if data["v1_snapshot_url"] != self.last_v1_snapshot_url: # Do not call cdn again already we have snapshot
                                    async with aiohttp.ClientSession() as cdn_sesion:
                                        async with cdn_sesion.get(
                                            data["v1_snapshot_url"],
                                            timeout=30,
                                        ) as cdn_res:
                                            if cdn_res.status == 200:
                                                self.last_v1_snapshot = await cdn_res.json()
                                                self.last_v1_snapshot_url = data["v1_snapshot_url"]
                                                self.last_clore_price = data["clore_price"]
                                                return gigaspot_snapshot(False, self.last_v1_snapshot, extrct_gs_shapshot_time(self.last_v1_snapshot_url), self.my_user_id, self.last_clore_price)
                                else:
                                    return gigaspot_snapshot(False, self.last_v1_snapshot, extrct_gs_shapshot_time(self.last_v1_snapshot_url), self.my_user_id, self.last_clore_price)
                        clore_res.raise_for_status()
                        return gigaspot_snapshot(True, {}, None, None, None)

            except aiohttp.ClientError as e:
                logger.error(f"get_gigaspot | HTTP Error on attempt {attempt + 1}: {e}")
            except asyncio.TimeoutError:
                logger.error(f"get_gigaspot | Request timed out on attempt {attempt + 1}")
            except Exception as e:
                logger.error(f"get_gigaspot | An unexpected error occurred on attempt {attempt + 1}: {e}")

            if attempt + 1 < retries:
                delay = random.uniform(2, 5) 
                logger.log(f"get_gigaspot | Retrying in {delay:.2f} seconds...")
                await asyncio.sleep(delay)
        return gigaspot_snapshot(True, {}, None, None, None)

    async def create_orders(self, orders: List[dict], retries=3):
        if not isinstance(orders, list):
            logger.error(f"create_orders | Expected a list, got {type(orders).__name__}")
            return create_result(True, [], [], [], [])
        
        if not all(isinstance(item, dict) for item in orders):
            logger.error("create_orders | All elements in the list must be dict")
            return create_result(True, [], [], [], [])
    
        submit_json = []

        for idx, order in enumerate(orders):
            if not "currency" in order:
                order["currency"] = DEFAULT_CURRENCY
            submit_json.append(order)
            if not validate_order(order, "create", idx):
                return create_result(True, [], [], [], [])

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                        CLORE_API + "/v1/create_gigaspot_orders",
                        headers=self.generate_headers(),
                        data=json.dumps(submit_json),
                        timeout=20,
                    ) as clore_res:
                        if clore_res.status == 429:
                            retry_after = clore_res.headers.get("Retry-After")
                            if retry_after:
                                delay = int(retry_after)  # Respect server's Retry-After header
                            else:
                                delay = random.uniform(2, 5)  # Fallback random delay
                            logger.error(f"create_orders | HTTP 429 received. Retrying after {delay:.2f} seconds...")
                            await asyncio.sleep(delay)
                            continue  # Retry the request
                        elif clore_res.status == 200:
                            data = await clore_res.json()
                            if "failed_to_oc_servers" in data:
                                failed_to_rent =list(set(data["failed_to_oc_servers"] + data["failed_to_rent_servers"]))
                                rented_ids = []
                                for order in orders:
                                    if not order["renting_server"] in failed_to_rent:
                                        rented_ids.append(order["renting_server"])

                                return create_result(
                                    False,
                                    data["failed_to_oc_servers"],
                                    data["failed_to_rent_servers"],
                                    data["too_low_bids_servers"],
                                    rented_ids
                                )
                        clore_res.raise_for_status()

            except aiohttp.ClientError as e:
                logger.error(f"create_orders | HTTP Error on attempt {attempt + 1}: {e}")
            except asyncio.TimeoutError:
                logger.error(f"create_orders | Request timed out on attempt {attempt + 1}")
            except Exception as e:
                logger.error(f"create_orders | An unexpected error occurred on attempt {attempt + 1}: {e}")

            if attempt + 1 < retries:
                delay = random.uniform(2, 5) 
                logger.log(f"create_orders | Retrying in {delay:.2f} seconds...")
                await asyncio.sleep(delay)

        return create_result(True, [], [], [], [])
        
    async def edit_orders(self, changes: List[dict], retries=3):
        if not isinstance(changes, list):
            logger.error(f"edit_orders | Expected a list, got {type(changes).__name__}")
            return edit_result(True, [], [], [])
        
        if not all(isinstance(item, dict) for item in changes):
            logger.error("edit_orders | All elements in the list must be dict")
            return edit_result(True, [], [], [])
    
        for idx, change in enumerate(changes):
            if not validate_order(change, "edit", idx):
                return edit_result(True, [], [], [])

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                        CLORE_API + "/v1/edit_gigaspot_orders",
                        headers=self.generate_headers(),
                        data=json.dumps(changes),
                        timeout=20,
                    ) as clore_res:
                        if clore_res.status == 429:
                            retry_after = clore_res.headers.get("Retry-After")
                            if retry_after:
                                delay = int(retry_after)  # Respect server's Retry-After header
                            else:
                                delay = random.uniform(2, 5)  # Fallback random delay
                            logger.error(f"cancel_orders | HTTP 429 received. Retrying after {delay:.2f} seconds...")
                            await asyncio.sleep(delay)
                            continue  # Retry the request
                        elif clore_res.status == 200:
                            data = await clore_res.json()
                            if "failed_to_update_ids" in data:
                                return edit_result(
                                    False,
                                    data["failed_to_update_ids"],
                                    data["success_to_update_ids"],
                                    data["too_low_bid_ids"]
                                )
                        clore_res.raise_for_status()

            except aiohttp.ClientError as e:
                logger.error(f"cancel_orders | HTTP Error on attempt {attempt + 1}: {e}")
            except asyncio.TimeoutError:
                logger.error(f"cancel_orders | Request timed out on attempt {attempt + 1}")
            except Exception as e:
                logger.error(f"cancel_orders | An unexpected error occurred on attempt {attempt + 1}: {e}")

            if attempt + 1 < retries:
                delay = random.uniform(2, 5) 
                logger.log(f"cancel_orders | Retrying in {delay:.2f} seconds...")
                await asyncio.sleep(delay)
        return edit_result(True, [], [], [])

    
    async def cancel_orders(self, order_ids: List[int], retries=3):
        if not isinstance(order_ids, list):
            logger.error(f"cancel_orders | Expected a list, got {type(order_ids).__name__}")
            return cancel_result(True, [], [])    

        if not all(isinstance(item, int) for item in order_ids):
            logger.error("cancel_orders | All elements in the list must be integers")
            return cancel_result(True, [], [])

        if len(order_ids) == 0:
            logger.error("cancel_orders | You need to pass at least one order")
            return cancel_result(True, [], [])
        
        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                        CLORE_API + "/v1/cancel_orders",
                        headers=self.generate_headers(),
                        data=json.dumps({"order_ids": order_ids}),
                        timeout=20,
                    ) as clore_res:
                        if clore_res.status == 429:
                            retry_after = clore_res.headers.get("Retry-After")
                            if retry_after:
                                delay = int(retry_after)  # Respect server's Retry-After header
                            else:
                                delay = random.uniform(2, 5)  # Fallback random delay
                            logger.error(f"cancel_orders | HTTP 429 received. Retrying after {delay:.2f} seconds...")
                            await asyncio.sleep(delay)
                            continue  # Retry the request
                        elif clore_res.status == 200:
                            data = await clore_res.json()
                            if "failed_to_cancel" in data:
                                return cancel_result(
                                    False,
                                    data["failed_to_cancel"],
                                    [num for num in order_ids if num not in data["failed_to_cancel"]]
                                )
                        clore_res.raise_for_status()

            except aiohttp.ClientError as e:
                logger.error(f"cancel_orders | HTTP Error on attempt {attempt + 1}: {e}")
            except asyncio.TimeoutError:
                logger.error(f"cancel_orders | Request timed out on attempt {attempt + 1}")
            except Exception as e:
                logger.error(f"cancel_orders | An unexpected error occurred on attempt {attempt + 1}: {e}")

            if attempt + 1 < retries:
                delay = random.uniform(2, 5) 
                logger.log(f"cancel_orders | Retrying in {delay:.2f} seconds...")
                await asyncio.sleep(delay)
        return cancel_result(True, None, None)