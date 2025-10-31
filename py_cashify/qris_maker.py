import requests
from typing import Optional

class QrisMaker:
    BASE_URL = "https://larabert-qrgen.hf.space/v1/create-qr-code"

    @staticmethod
    def make_qr(qr_string: str, size: str = "500x500", style: int = 2, color: str = "ea580c") -> Optional[bytes]:
        params = {
            "size": size,
            "style": style,
            "color": color,
            "data": qr_string
        }
        response = requests.get(QrisMaker.BASE_URL, params=params)
        if response.status_code == 200:
            return response.content  # returns image bytes
        return None
