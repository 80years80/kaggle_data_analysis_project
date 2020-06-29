import os
import tweepy as tw
import pandas as pd

consumer_key = 'DdlDuwIKYPcCgzBPbmLMQ1MnZ'
consumer_secret = 'auQeotTVzwsqEqzFKyN6vFK1ssmBfrs2ljuaGhmKWyXqSgpvwM'
access_token = '1277000343209906176-iucgGXWza08tcI76mBYpWTTRtIqss9'
access_token_secret = 'HWeztnZppPPYaHWtTmxHsd4sTYd4DI2IdyABDps8088Xu'

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