from flask import Flask, render_template, request, jsonify

# create an isntance of the Flask class
app = Flask(__name__)

# define a route for the home page
@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/rfid')
def rfid():
    return "This is the rfid page!"

# run the app
if __name__ == "__main__":
    app.run(debug=True)