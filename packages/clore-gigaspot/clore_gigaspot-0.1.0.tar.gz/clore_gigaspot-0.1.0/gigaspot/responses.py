class gigaspot_snapshot:
    def __init__(self, failure: bool, snapshot: dict, timestamp: int, my_id: int):
        self.failure = failure
        self.snapshot = snapshot
        self.timestamp = timestamp
        self.my_id = my_id

class create_result:
    def __init__(self, failure: bool, failed_to_oc: list[int], failed_to_rent: list[int], rented_ids: list[int]):
        self.failure = failure
        self.failed_to_oc = failed_to_oc
        self.failed_to_rent = failed_to_rent
        self.rented_ids = rented_ids

class edit_result:
    def __init__(self, failure: bool, failed_to_update_ids: list[int], success_to_update_ids: list[int]):
        self.failure = failure
        self.failed_to_update_ids = failed_to_update_ids
        self.success_to_update_ids = success_to_update_ids

class cancel_result:
    def __init__(self, failure: bool, failed_to_cancel: list[int], canceled: list[int]):
        self.failure = failure
        self.failed_to_cancel = failed_to_cancel
        self.canceled = canceled