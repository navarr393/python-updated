from flask import Flask, request, redirect
import random

app = Flask(__name__)

next_url_path = 0
url_mappings = {}
letters = "abcdefghijklmnopqrstuvwxyz"
shortened_lenght = 8

@app.post("/shorten")
def create_new_short_url():
    long_url = request.json["url"]
    short_url = "/s/"

    for i in range(shortened_lenght):
        short_url += random.choice(letters)

    if short_url not in url_mappings:
        url_mappings[short_url] = long_url
        return short_url
    else:
        return "There was an error."
    

@app.get("/s/<id>")
def redirect_to_url(id):
    long_url = url_mappings.get(f"/s/{id}") # returns the shortned url

    if long_url:
        return redirect(long_url)   # returns the long_url which has the path to short_url
    else:
        return "There was no url found."
    

if __name__ == "__main__":
    app.run(debug=True)