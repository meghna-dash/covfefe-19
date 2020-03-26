import tweepy
import datetime
#tweet py setup stuff
consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# list of twitter to check
accounts=[
    'WHO',
    'JHSPH_CHS'
]

#number of days to check
num_days=4
oldest_date = datetime.today() - timedelta(days=num_days)

tweets=[]

for account in accounts:
    for tweet in tweepy.Cursor(api.user_timeline, id=account).items():
        if tweet.created_at < oldest_date:
            break;
        tweets.append(tweet)

