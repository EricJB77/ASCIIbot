import tweepy
import time
from config import getkeysandtokens


# Get secret api keys and access tokens from config file
flagfile = 'apikey'
consumer_key = getkeysandtokens(flagfile)

flagfile = 'apisecretkey'
consumer_secret = getkeysandtokens(flagfile)

flagfile = 'accesstoken'
key = getkeysandtokens(flagfile)

flagfile = 'accesstokensecret'
secret = getkeysandtokens(flagfile)


# Set the authentication information
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# Choose the hashtag to retweet
hashtag = "SpaceX"
tweetNumber = 5 # number of tweets to grab based on that hashtag

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)


searchBot()


