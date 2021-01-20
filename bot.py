
import tweepy
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

# Set it to work with tweepy
api = tweepy.API(auth)

# Used to create a tweet
#api.update_status('Twittr bot reporting in live')


#API.mentions_timeline([since_id][, max_id][, count])
tweets = api.mentions_timeline()
#print(tweets[0].text)


# Returns all tweets mentioning "@ASCIIbot"
for tweet in tweets:
    print(str(tweet.id) + ' - ' + tweet.text)

# If a certain work was mentioned in a tweet, print out that tweet
for tweet in tweets:
    print(str(tweet.id) + ' - ' + tweet.text)
#    if 'hi' in tweet.text.lower():
#        print(str(tweet.id) + ' - ' + tweet.text)







