from flask import Flask, render_template, request
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

app = Flask(__name__)

# Define the route for the home page and allow both GET and POST requests
@app.route("/", methods=['GET', 'POST'])
def home():
    # Initialize variables to hold the user's input text, sentiment scores, and sentiment type
    sentiment = None
    input_text = None
    sentiment_type = None

    if request.method == 'POST':
        # Get the input text from the form in the index.html file
        input_text = request.form.get('input')
        # Get the polarity scores of the input text and assign it to the sentiment variable
        sentiment = analyzer.polarity_scores(input_text)
        # Get the compound score from the sentiment dictionary
        compound = sentiment['compound']

        # Determine the sentiment type based on the compound score
        if compound > 0.1:
            sentiment_type = "Positive comment!"
        elif compound < -0.1:
            sentiment_type = "Negative comment..."
        else:
            sentiment_type = "Neutral comment."

    # Send the variables back to index.html to display on the web page
    return render_template('index.html', sentiment=sentiment, input_text=input_text, sentiment_type=sentiment_type)

if __name__ == "__main__":
    app.run(debug=True)
