import requests
import base64

# Your actual keys
SECRET_KEY = "sk_test_5JBaqmjyzTxm9uvymjPinHkv"

# Create auth header
auth_string = f"{SECRET_KEY}:"
auth_header = base64.b64encode(auth_string.encode()).decode()

# Test creating a payment intent
url = "https://api.paymongo.com/v1/payment_intents"
headers = {
    "Authorization": f"Basic {auth_header}",
    "Content-Type": "application/json"
}
payload = {
    "data": {
        "attributes": {
            "amount": 10000,  # ₱100.00
            "payment_method_allowed": ["card"],
            "description": "Test payment",
            "currency": "PHP"
        }
    }
}

response = requests.post(url, json=payload, headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")