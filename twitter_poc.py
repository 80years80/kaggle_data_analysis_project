import os
import tweepy as tw
import pandas as pd
import json

f = open('/home/pi/twitter_api_creds.json')
creds = json.load(f)
consumer_key = creds['consumer_key']
consumer_secret = creds['consumer_secret']
access_token = creds['access_token']
access_token_secret = creds['access_token_secret']

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "#wildfires"
search_refined = search_words + " -filter:retweets"
date_since = "2018-11-16"
# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
for tweet in tweets:
    print(tweet.text)