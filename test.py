import requests

url = "http://192.168.1.97:8081/helpdesk/WebObjects/Helpdesk.woa/ra/Tickets/20894"
params = {
    "username": "",
    "password": ""
}
ticket_data = {
    "emailClient": False,
    "emailTech": False,
    "emailTechGroupLevel": False,
    "emailGroupManager": False,
    "emailCc": False,
    "emailBcc": False,
    "subject": "App to manage Solar Winds Tickets",
    "detail": "Working on WebHelpDesk API to implement on the IT Kiosk project.",
    "assignToCreatingTech": True,
    "problemtype": {"type": "RequestType", "id": 11},
    "sendEmail": False,
    "location": {"type": "Location", "id": 7},
    "department": {"type": "Department", "id": 15},
    "statustype": {"type": "StatusType", "id": 3},
    "prioritytype": {"type": "PriorityType", "id": 3},
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, params=params, json=ticket_data, headers=headers)

if response.ok:
    print("Ticket created successfully!")
    try:
        data = response.json()
        print("Response JSON:")
        print(data)
    except ValueError:
        print("Response is not in JSON format.")
else:
    print("Failed to create ticket. Status code:", response.status_code)
    print("Response text:", response.text)
