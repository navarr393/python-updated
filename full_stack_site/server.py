from flask import Flask, request, render_template
import requests

app = Flask(__name__)
api_key = "89d9aefd54e477a8430fda661ce16692"
# run the html file using @app.route()
@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        location = request.form.get('location')
        params = {
            "appid": api_key,
            "q": location,
            "units": "imperial"
        }
        response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params)
        weather_data = response.json()

    return render_template('index.html', weather=weather_data)

# creating more endpoints 
@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contanct_page():
    return render_template("contact.html")

@app.route("/form")
def form_page():
    return render_template("form_page.html")

@app.post("/create-weather")
def create_acount():
    city = request.form.get("city")
    #last_name = request.form.get("last_name")
    
    return render_template("account_created.html", city=city)

if __name__ == "__main__":
    app.run(debug=True)