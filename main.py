from os import access
import jwt.utils
import time
import math

accessKey = {
  "developer_id": "5db7904f-45d3-46ba-8f58-80eb576edcf4",
  "key_id": "1673c7c9-b6f7-4845-9dc1-d7dbf6279b3b",
  "signing_secret": "XUZ3t4cfayZaJh6wV7NhrRVQAraoDwrTiylmx5wYZgM"
}

token = jwt.encode(
    {
        "aud": "doordash",
        "iss": accessKey["developer_id"],
        "kid": accessKey["key_id"],
        "exp": str(math.floor(time.time() + 60)),
        "iat": str(math.floor(time.time())),
    },
    jwt.utils.base64url_decode(accessKey["signing_secret"]),
    algorithm="HS256",
    headers={"dd-ver": "DD-JWT-V1"})

print(token)

import requests

endpoint = "https://openapi.doordash.com/drive/v2/deliveries/"

headers = {"Authorization": "Bearer " + token,
            "Content-Type": "application/json"}

request_body = { # Modify pickup and drop off addresses below
    "external_delivery_id": "1673c7c9-b6f7-4845-9dc1-d7dbf6279b3b",
    "pickup_address": "901 Market Street 6th Floor San Francisco, CA 94103",
    "pickup_business_name": "Wells Fargo SF Downtown",
    "pickup_phone_number": "+16505555555",
    "pickup_instructions": "Enter gate code 1234 on the callbox.",
    "dropoff_address": "901 Market Street 6th Floor San Francisco, CA 94103",
    "dropoff_business_name": "Wells Fargo SF Downtown",
    "dropoff_phone_number": "+16505555555",
    "dropoff_instructions": "Enter gate code 1234 on the callbox.",
    "order_value": 1999
}

create_delivery = requests.post(endpoint, headers=headers, json=request_body) # Create POST request


print(create_delivery.status_code)
print(create_delivery.text)
print(create_delivery.reason)