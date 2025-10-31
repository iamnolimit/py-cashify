import requests
from typing import Any, Dict, Optional

class CashifyAPI:
    BASE_URL = "https://cashify.my.id/api/generate"

    def __init__(self, license_key: str):
        self.license_key = license_key
        self.headers = {
            "x-license-key": self.license_key,
            "content-type": "application/json"
        }

    def create_transaction(self, qris_id: str, amount: float, use_unique_code: bool, package_ids: list, expired_in_minutes: int) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/qris"
        payload = {
            "id": qris_id,
            "amount": amount,
            "useUniqueCode": use_unique_code,
            "packageIds": package_ids,
            "expiredInMinutes": expired_in_minutes
        }
        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def check_transaction(self, transaction_id: str) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/check-status"
        payload = {
            "transactionId": transaction_id
        }
        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()
