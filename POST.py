 
import requests
api_key = "GjFITtVLtSX3TGT3lhDu"
url = "https://ramalakshmilakshmi-assist.freshdesk.com/api/v2/tickets"
ticket = {
    "subject": "My laptop is not working",  
    "description": "My laptop is not working",
    "email": "ramu@gmail.com",
    "priority": 2, 
    "status": 2
}
response = requests.post(url, auth=(api_key, "X"), json=ticket)
if response.status_code == 201: 
    print("Ticket created successfully", response.json())
else:
    print("Ticket creation failed")  


import requests

api_key = "GjFITtVLtSX3TGT3lhDu"
url = "https://ramalakshmilakshmi-assist.freshdesk.com/api/v2/tickets"

ticket = {
    "subject": "My laptop is not working",  
    "description": "My laptop is not working",
    "email": "ramugmail.com",
    "priority": 2, 
    "status": 2
}

response = requests.post(url, auth=(api_key, "X"), json=ticket)

# Assert statement to check if status code is 201
assert response.status_code == 201 
print("Ticket created successfully!")
print(response.json())

