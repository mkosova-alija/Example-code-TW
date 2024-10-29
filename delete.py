import tweepy

from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Initialize the Tweepy client with the necessary credentials
client = tweepy.Client (
    consumer_key=API_KEY, consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)

# Inform the tweed ID that you wand to delete
tweet_id = '1850876810013049055'

# Delete the tweet using client.delete_tweet method
response = client.delete_tweet(tweet_id)

# Print response to the terminal
print(response)