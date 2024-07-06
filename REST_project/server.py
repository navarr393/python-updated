from flask import Flask, request

# Create a new flask server

app = Flask(__name__)   # pass the name of the file in this case 'server'

next_id = 5 # this will be assigned to the new id we create

contacts = [
    {"id": "1", "name": "Shaun", "phone": "123-456-3212" },
    {"id": "2", "name": "David", "phone": "153-456-1212" },
    {"id": "3", "name": "Omar", "phone": "323-456-1212" },
    {"id": "4", "name": "Daniel", "phone": "123-456-0212" },
]

# create endpoint /hello    GET - Method
@app.route("/hello")
def hello_route():
    print("I have received a request on the /hello endpoint.")
    return "<h1>Hello from the server!</h1>"

@app.get("/contacts")   # returs specific data in this case only all contacts
def list_contacts():
    return contacts

@app.get("/contacts/<string:id>")   #GET is for listing an individual contact
def read_single_contact(id):    # note we pass the argument 'id' here as well
    for contact in contacts:
        if contact["id"] == id:
            return contact
    return "That contact does not exist!"

@app.post("/contacts")  # POST is for creating new contacts, this will require a request
def create_contact():   # this func will append the new contanct we create to contacts dictionary and update the "id", contacts are created using postMan.
    global next_id

    new_contact = {
        "id": f"{next_id}",
        "name": request.json["name"],
        "phone": request.json["phone"]
    }

    contacts.append(new_contact)
    next_id += 1
    return new_contact

@app.put("/contacts/<id>")  # this uses the PUT and updates the id, with this function we can update the id.
def update_contact(id):
    for contact in contacts:
        if contact["id"] == id:
            contact["name"] = request.json["name"] if "name" in request.json else contact["name"] # only update if it is being requested otherwise leave the same.
            contact["phone"] = request.json["phone"] if "phone" in request.json else contact["phone"]
            return contact
    return "There is no contact with that id!"


@app.delete("/contacts/<string:id>") #DELETE, deletes the contact specified based on the <id> that we pass in the url
def delete_contact(id):
    for contact in contacts:
        if contact["id"] == id:
            contacts.remove(contact)
            return contact
    return "There is no contact with that id!"

if __name__ == "__main__":
    app.run(debug=True) # starts the server1