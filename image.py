import tweepy

from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN

# Initialize OAuthHandler with API key and secret for authentication
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
# Set access token and secret for user authentication
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Create API object with rate limit handling
api = tweepy.API(auth, wait_on_rate_limit=True)

# Initialize the Tweepy client with the necessary credentials
client = tweepy.Client (BEARER_TOKEN, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, wait_on_rate_limit=True)

# Upload the media file to X and get the media ID
media_id= api.media_upload(filename="hamk.png").media_id_string
# Print the media ID to the terminal
print(media_id)

# Tweet content
text = "Testing how well this works"

# Create a tweet with the text created earlier and attached media
client.create_tweet(text=text, media_ids=[media_id])
# Print a confirmation message to the terminal
print("Tweet works")
