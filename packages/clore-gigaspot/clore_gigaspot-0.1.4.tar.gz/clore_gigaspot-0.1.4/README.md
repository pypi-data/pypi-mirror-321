# CLORE GigaSPOT python SDK

Before proceeding with usage familiarize yourself with
- https://docs.clore.ai/gigaspot/overview
- https://gigaspot-api-docs.clore.ai/

#### Import in python & setup connection

```python
import clore_gigaspot

gigaspot_connection = clore_gigaspot.gigaspot_connection(
    gigaspot_api_key="<your clore.ai API key>"
)
```

## Get GigaSPOT snapshot

```python
r = await gigaspot_connection.get_gigaspot()

print(r.failure) # True/False bool if call could not be executed
print(r.snapshot) # GigaSPOT snapshot itself
print(r.timestamp) # Unix Timestamp of GigaSPOT snapshot
print(r.my_id) # My CLORE.AI account ID - useful for finding my orders in GigaSPOT snapshot
print(r.clore_price) # Price of CLORE Blockchain in dollars
```

Example snapshot showcased on https://gigaspot-api-docs.clore.ai/

## Create GigaSPOT order(s)

```python
create_res = await gigaspot_connection.create_orders(
    [
        {
            "currency": "CLORE-Blockchain",      # Currency of rental
            "image": "c9a4e2f6b7d488d8f0bab0ff", # CCR image of rental (in this case HiveOS)
            "renting_server": 35005,             # ID of server to rent
            "price": 28.9755,                    # bid amount
            "oc": [                              # Overclocking settings, must pass config per GPU
                {
                    "pl": 150,           # GPU 0 Power Limit (W)
                    "mem_lock": 6800,    # GPU 0 Memory Clock Lock (MHz)
                    "core_lock": 900,    # GPU 0 Core Clock Lock (MHz)
                    "mem_offset": 1000,  # GPU 0 Memory Clock Offset (MHz)
                    "core_offset": 0     # GPU 0 Core Clock Offset (MHz)
                },
                {
                    "pl": 150,           # GPU 1 Power Limit (W)
                    "mem_lock": 6800,    # GPU 1 Memory Clock Lock (MHz)
                    "core_lock": 900,    # GPU 1 Core Clock Lock (MHz)
                    "mem_offset": 1000,  # GPU 1 Memory Clock Offset (MHz)
                    "core_offset": 0     # GPU 1 Core Clock Offset (MHz)
                },
                {
                    "pl": 150,           # GPU 2 Power Limit (W)
                    "mem_lock": 6800,    # GPU 2 Memory Clock Lock (MHz)
                    "core_lock": 900,    # GPU 2 Core Clock Lock (MHz)
                    "mem_offset": 1000,  # GPU 2 Memory Clock Offset (MHz)
                    "core_offset": 0     # GPU 2 Core Clock Offset (MHz)
                },
                {
                    "pl": 150,           # GPU 3 Power Limit (W)
                    "mem_lock": 6800,    # GPU 3 Memory Clock Lock (MHz)
                    "core_lock": 900,    # GPU 3 Core Clock Lock (MHz)
                    "mem_offset": 1000,  # GPU 3 Memory Clock Offset (MHz)
                    "core_offset": 0     # GPU 3 Core Clock Offset (MHz)
                },
                {
                    "pl": 150,           # GPU 4 Power Limit (W)
                    "mem_lock": 6800,    # GPU 4 Memory Clock Lock (MHz)
                    "core_lock": 900,    # GPU 4 Core Clock Lock (MHz)
                    "mem_offset": 1000,  # GPU 4 Memory Clock Offset (MHz)
                    "core_offset": 0     # GPU 4 Core Clock Offset (MHz)
                },
                {
                    "pl": 150,           # GPU 5 Power Limit (W)
                    "mem_lock": 6800,    # GPU 5 Memory Clock Lock (MHz)
                    "core_lock": 900,    # GPU 5 Core Clock Lock (MHz)
                    "mem_offset": 1000,  # GPU 5 Memory Clock Offset (MHz)
                    "core_offset": 0     # GPU 5 Core Clock Offset (MHz)
                }
            ],
            "env": {                     # ENV variables
                "rig_id": "10474277",    # HiveOS rig_id
                "rig_pass": "SsN1bVZh"   # HiveOS rig_pass
            }
        }
    ]
)

print(create_res.failure) # True/False bool if call could not be executed
print(create_res.failed_to_oc) # IDs of machines, to which OC settings can't be applied as it's out of allowed range (range specified in GigaSPOT snapshot)
print(create_res.failed_to_rent) # IDs of machines, Failed to rent for any reason - already on demand rented, offline, failed_to_oc,...
print(create_res.too_low_bids_servers) # IDs of machines to which your bid is bellow minimum allowed bid
print(create_res.rented_ids) # IDs of machines on which your bids were created
```

## Edit GigaSPOT order(s)

```python
edit_res = await gigaspot_connection.edit_orders(
    [
        {
            "order_id": 602837,          # GigaSPOT order id, can be retrieved from GigaSPOT snapshot or https://clore.ai/api-docs (my_orders call)
            "price": 29.05,              # New updated bid price
            "oc": [                      # Overclocking settings update (optional)
                {
                    "pl": 130,           # GPU 0 Power Limit (W)
                    "mem_lock": 5000,    # GPU 0 Memory Clock Lock (MHz)
                    "core_lock": 1350,   # GPU 0 Core Clock Lock (MHz)
                    "mem_offset": 0,     # GPU 0 Memory Clock Offset (MHz)
                    "core_offset": 0     # GPU 0 Core Clock Offset (MHz)
                },
                {
                    "pl": 130,           # GPU 1 Power Limit (W)
                    "mem_lock": 5000,    # GPU 1 Memory Clock Lock (MHz)
                    "core_lock": 1350,   # GPU 1 Core Clock Lock (MHz)
                    "mem_offset": 0,     # GPU 1 Memory Clock Offset (MHz)
                    "core_offset": 0     # GPU 1 Core Clock Offset (MHz)
                },
                {
                    "pl": 130,           # GPU 2 Power Limit (W)
                    "mem_lock": 5000,    # GPU 2 Memory Clock Lock (MHz)
                    "core_lock": 1350,   # GPU 2 Core Clock Lock (MHz)
                    "mem_offset": 0,     # GPU 2 Memory Clock Offset (MHz)
                    "core_offset": 0     # GPU 2 Core Clock Offset (MHz)
                },
                {
                    "pl": 130,           # GPU 3 Power Limit (W)
                    "mem_lock": 5000,    # GPU 3 Memory Clock Lock (MHz)
                    "core_lock": 1350,   # GPU 3 Core Clock Lock (MHz)
                    "mem_offset": 0,     # GPU 3 Memory Clock Offset (MHz)
                    "core_offset": 0     # GPU 3 Core Clock Offset (MHz)
                },
                {
                    "pl": 130,           # GPU 4 Power Limit (W)
                    "mem_lock": 5000,    # GPU 4 Memory Clock Lock (MHz)
                    "core_lock": 1350,   # GPU 4 Core Clock Lock (MHz)
                    "mem_offset": 0,     # GPU 4 Memory Clock Offset (MHz)
                    "core_offset": 0     # GPU 4 Core Clock Offset (MHz)
                },
                {
                    "pl": 130,           # GPU 5 Power Limit (W)
                    "mem_lock": 5000,    # GPU 5 Memory Clock Lock (MHz)
                    "core_lock": 1350,   # GPU 5 Core Clock Lock (MHz)
                    "mem_offset": 0,     # GPU 5 Memory Clock Offset (MHz)
                    "core_offset": 0     # GPU 5 Core Clock Offset (MHz)
                }
            ],
        }
    ]
)

print(edit_res.failure) # True/False bool if call could not be executed
print(edit_res.failed_to_update_ids) # IDs of orders, that could not be updated for any reason
print(edit_res.success_to_update_ids) # IDs of orders, that updated successfully
print(edit_res.too_low_bid_ids) # IDs of orders, that their new bid was too low
```

## Cancel GigaSPOT order(s)

```python
cancel_res = await gigaspot_connection.cancel_orders(
    [602837] # IDs of orders to cancel
)

print(cancel_res.failure) # True/False bool if call could not be executed
print(cancel_res.failed_to_cancel) # IDs of orders, that could not be canceled for any reason
print(cancel_res.canceled) # IDs of orders, that were canceled successfully
```