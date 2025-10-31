from croniter import croniter
from datetime import datetime
import time
from .api import CashifyAPI

class CashifyCronChecker:
    def __init__(self, license_key: str, transaction_id: str, cron_expr: str):
        self.api = CashifyAPI(license_key)
        self.transaction_id = transaction_id
        self.cron_expr = cron_expr

    def auto_check(self, callback=None, max_checks: int = 10):
        base = datetime.now()
        cron = croniter(self.cron_expr, base)
        checks = 0
        while checks < max_checks:
            next_check = cron.get_next(datetime)
            sleep_time = (next_check - datetime.now()).total_seconds()
            if sleep_time > 0:
                time.sleep(sleep_time)
            result = self.api.check_transaction(self.transaction_id)
            if callback:
                callback(result)
            checks += 1
            if result.get('status') == 'completed':
                break
        return result
