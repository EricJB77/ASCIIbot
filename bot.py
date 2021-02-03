
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

# Set it to work with tweepy
api = tweepy.API(auth)

# Used to create a tweet
#api.update_status('Twitter bot reporting in live')


# Returns all tweets mentioning "@ASCIIbot"
'''
for tweet in tweets:
    print(str(tweet.id) + ' - ' + tweet.text)
'''


FILE_NAME = 'last_seen.txt'


# Reads the lasts tweet ID accessed
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

# Writes the lasts tweet ID accessed
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return



# If a certain word was mentioned in a tweet, print out that tweet, reply, like and re-tweet
def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
    for tweet in reversed(tweets):
        print(tweet.id, tweet.full_text.lower())
        if '#hi' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + "You have unlocked the auto reply, like and retweet function :)", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


reply()

'''
while True:
    reply()
    time.sleep(15)
'''

