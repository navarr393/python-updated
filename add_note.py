import requests

url = "http://192.168.1.97:8081/helpdesk/WebObjects/Helpdesk.woa/ra/TechNotes"
params = {
    "username": "",
    "password": ""
}

# you must pass the id of the ticket you want to edit
ticket_data = {
    "noteText":"Today I read the API documentation and managed to fetch user tickets, create a new ticket and resolve a ticket.",
    "jobticket": {"type":"JobTicket","id":20884},
    "workTime":"270",
    "isHidden":False,
    "isSolution": False,
    "statusTypeId":3,
    "emailClient":False,
    "emailTech":False,
    "emailTechGroupLevel": False,
    "emailGroupManager": False,
    "emailCc": False,
    "emailBcc": False,
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, params=params, json=ticket_data, headers=headers)

if response.ok:
    print("added note to ticket successfully!")
    try:
        data = response.json()
        print("Response JSON:")
        print(data)
    except ValueError:
        print("Response is not in JSON format.")
else:
    print("Failed to create ticket. Status code:", response.status_code)
    print("Response text:", response.text)