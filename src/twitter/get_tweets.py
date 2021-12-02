from src.twitter.twittersecrets import *

import tweepy
import requests
import time

# add to these to search more of Twitter! :)
tags_to_search = ["%23pictures", "hanging out", "hangout", "friends", "pals", "missed you", "sorority", "fraternity",
                  "alpha phi", "rush week", "%23college", "greek life", "%23gogreek", "weekend", "beautiful day",
                  "%23optoutside", "night out", "Friday night", "bar crawl", "pub crawl", "%23TGIF", "hosting"]

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
"""
# to get token if not already saved to secrets.py:
try:
    redirect_url = auth.get_authorization_url()
    print(redirect_url)

except tweepy.TweepError:
    print('Error! Failed to get request token.')


verifier = input('Verifier:')
auth.get_access_token(verifier)
print(auth.access_token)
print(auth.access_token_secret)
"""
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


api = tweepy.Client(bearer_token=BEARER_TOK, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
i = 0
total = 0

while True:

    result = api.search_recent_tweets(query="(#AEWDynamite) lang:en -is:retweet", since_id="1466218790308491265")#(tags_to_search[i], lang="en", result_type="recent", count="50", include_entities=False)
    print(result)
    total += result.count
    for r in result:
        userid = r.author.id_str
        username = r.author.screen_name
        statusid = r.id
        print(r.body)

    print("finished tag " + tags_to_search[i])
    i = (i + 1) % len(tags_to_search)
    if(i == 0):
        time.sleep(1000)

    if total > 100000: # rate limit at least a little
        break
