# import the tweepy library
import tweepy

# initialize the client by passing it your API credential information for the authentication part
#these keys and tokens are created with Read and Write permissions in the Twitter App
client = tweepy.Client(consumer_key='ADD_YOUR_KEY_HERE',
                       consumer_secret='ADD_YOUR_SECRET_HERE',
                       access_token='ADD_YOUR_TOKEN_HERE',
                       access_token_secret='ADD_YOUR_TOKEN_SECRET_HERE')

# with the help of client.create_tweet methot it is possible to create a tweet. The text parameter is the content of the tweet, in that you pass string as a tweet content.
response = client.create_tweet(text='Testing Tweepy functionalities')
#print your tweet to make sure it workds
print(response)
