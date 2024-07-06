# this file is the server where all the endpoints are defined, using flask
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/form")
def form_page():
    return render_template("form_page.html")

@app.post("/create_weather")
def submit_city():
    city = request.form.get("city")

    return render_template("weather_created.html", city=city)
# run the app
if __name__ == "__main__":
    app.run(debug=True)