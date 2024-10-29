import tweepy

# import credentials
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# initialize the client by passing it your API credential information for the authentication part
# these keys and tokens are created with Read and Write permissions in the Twitter App
client = tweepy.Client(
    consumer_key=API_KEY, consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)

# with the help of client.create_tweet methot it is possible to create a tweet. 
# The text parameter is the content of the tweet, in that you pass string as a tweet content.
response = client.create_tweet(text='Testing Tweepy functionalities')

#print your tweet to make sure it works
print(response)