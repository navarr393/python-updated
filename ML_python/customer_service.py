import nltk

from nltk.sentiment import SentimentIntensityAnalyzer
# download the pacakges to determine the sentiment of a text.
# nltk.download('vader_lexicon')
# nltk.download('subjectivity')
# nltk.download('movie_reviews')

analyzer = SentimentIntensityAnalyzer()

# A compound score between 0.05 and 1 indicates a positive sentiment.
# A compound score between -0.05 and -1 indicates a negative sentiment.
# A compound score between -0.05 and 0.05 indicates a neutral sentiment.

while True:
    next_text = input("Please enter your review: ")
    scores = analyzer.polarity_scores(next_text)
    compound = scores['compound']

    if compound > 0.1:
        print("Positive comment!")
    elif compound < -0.1:
        print("Negative comment...")
    else:
        print("Neutral comment.")