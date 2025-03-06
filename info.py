import requests
# mainly use this file to send random requests for info
"""
Locations and their ids:
Location Name: Banquets id: 24
Location Name: Bars id: 23
Location Name: Bike Cafe id: 29
Location Name: Brewery id: 13
Location Name: Cage id: 10
Location Name: Dynasty id: 25
Location Name: Event Center id: 27
Location Name: Freedom Court id: 3
Location Name: Gold/Dragon Room id: 5
Location Name: Hotel id: 26
Location Name: LOP id: 6
Location Name: Lotus Room id: 30
Location Name: Luyixian id: 18
Location Name: Macau id: 15
Location Name: Main Floor id: 7
Location Name: Pavilion id: 4
Location Name: Plaza Section id: 9
Location Name: Rewards Center  id: 21
Location Name: Second Floor id: 2
Location Name: Security id: 16
Location Name: Sen Pho id: 11
Location Name: Sora Sushi id: 19
Location Name: Tournament id: 31
Location Name: Uniforms id: 28
Location Name: Warehouse id: 12
Location Name:  id: 20

Departments: 
Department Name: Accounting id: 2
Department Name: Cage id: 11
Department Name: California Games id: 9
Department Name: Card Control id: 19
Department Name: Compliance id: 5
Department Name: Executive id: 4
Department Name: Facilities id: 8
Department Name: Food and Beverage id: 12
Department Name: Hotel id: 16
Department Name: Human Resources id: 1
Department Name: Marketing id: 6
Department Name: MIS id: 15
Department Name: Payroll id: 3
Department Name: Poker Games id: 10
Department Name: Security id: 14
Department Name: Surveillance id: 7
Department Name: Warehouse id: 13

Ticket status types:
status Name: Open id: 1
status Name: Pending id: 2
status Name: Closed id: 3
status Name: Cancelled id: 4
status Name: Resolved id: 5

Ticket priority types:
priority Name: Urgent id: 1
priority Name: High id: 2
priority Name: Medium id: 3
priority Name: Low id: 4

Problem type names:
priority Name: Audio/Visual Hardware id: 41
priority Name: Audio/Visual Software id: 42
priority Name: BeerSaver id: 26
priority Name: Berg id: 25
priority Name: Casino Management MTL id: 38
priority Name: Casino Management Printer id: 37
priority Name: Casino Management Server Administration id: 40
priority Name: Casino Management User Administration id: 39
priority Name: Casino Manangement Installation id: 36
priority Name: Email/Outlook id: 13
priority Name: Facilities id: 10
priority Name: Hardware id: 1
priority Name: Hardware Peripheral id: 30
priority Name: HR id: 3
priority Name: IT General/Other id: 12
priority Name: Kronos Administration id: 43
priority Name: Kronos clock reset id: 44
priority Name: Kronos lunch report id: 45
priority Name: Micros APP id: 18
priority Name: Micros CAPS id: 19
priority Name: Micros DB id: 17
priority Name: Micros ICARE id: 20
priority Name: Micros KDS id: 23
priority Name: Micros myINVENTORY id: 21
priority Name: Micros Printer id: 24
priority Name: Micros Workstation id: 22
priority Name: Microsoft Apps id: 29
priority Name: Microsoft Office id: 31
priority Name: Network id: 8
priority Name: New Request id: 46
priority Name: Phone ACD id: 35
priority Name: Phone Hardware id: 34
priority Name: Phone Software id: 33
priority Name: Phone/Voicemail id: 9
priority Name: POS Hardware id: 7
priority Name: POS Software id: 5
priority Name: Printer/Toner id: 6
priority Name: Software Microsoft Office id: 4
priority Name: Software Other id: 11
priority Name: Test Case id: 16
priority Name: User Administration id: 2
priority Name: Windows Apps id: 28
priority Name: Windows OS id: 27
"""
# Define the base URL
# pass the endpoint you want to test in this case RequestTypes
url = "http://192.168.1.97:8081/helpdesk/WebObjects/Helpdesk.woa/ra/RequestTypes"

# Set the query parameters as a dictionary
params = {
    "username": "",
    "password": ""
}

# Make the GET request, change the type of func you want to use, post put ect
# Note: 'verify=False' is used here to disable SSL certificate verification,
response = requests.get(url, params=params, verify=False)

# Check if the request was successful
if response.ok:
    print("Response received:")
    print(response.json())
    data = response.json()
    print("Total request types = ", len(data))
    for i in range(len(data)):
        print("priority Name:", data[i]["problemTypeName"], "id:", data[i]["id"])

else:
    print("Request failed with status code:", response.status_code)
