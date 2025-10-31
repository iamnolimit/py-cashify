
# py-cashify

Python library for interacting with Cashify QRIS API.

## Features
- Create transaction
- Check transaction status
- Auto check transaction status using croniter
- Generate QRIS QR Code

## Installation
Install from PyPI (after publish):
```bash
pip install py-cashify
```

Install for development:
```bash
pip install -r requirements.txt
```

## Usage

### Create Transaction
```python
from py_cashify import CashifyAPI

api = CashifyAPI(license_key="YOUR_LICENSE_KEY")
response = api.create_transaction(
    qris_id="qris123",
    amount=10000,
    use_unique_code=True,
    package_ids=["package1"],
    expired_in_minutes=10
)
print(response)
```

### Check Transaction
```python
status = api.check_transaction(transaction_id="TRANSACTION_ID")
print(status)
```

### Auto Check Transaction (croniter)
```python
from py_cashify import CashifyCronChecker


    print("Checked status:", result)

cron_checker = CashifyCronChecker(
    license_key="YOUR_LICENSE_KEY",
    transaction_id="TRANSACTION_ID",
    cron_expr="*/1 * * * *"  # every minute
)
cron_checker.auto_check(callback=callback, max_checks=5)
```

### Generate QRIS QR Code
```python
from py_cashify import QrisMaker

qr_bytes = QrisMaker.make_qr(qr_string="YOUR_QR_STRING", size="500x500", style=2, color="ea580c")
if qr_bytes:
    with open("qris.png", "wb") as f:
        f.write(qr_bytes)
    print("QR code saved as qris.png")
else:
    print("Failed to generate QR code")
```
