# get latest questions
# get latest answers
# write last tweet time in a file
# check if that file exist, then tweet accordingly

import requests
import json
import time
import tweepy

with open("lasttime.txt") as f:
    last_time = f.read()

questions = requests.get(f"https://api.stackexchange.com/2.3/questions?fromdate={last_time}&order=desc&sort=creation&site=tezos").json()

def tweet_question(data):
    twitter_auth_keys = {
        "consumer_key"        : "REPLACE_THIS_WITH_YOUR_CONSUMER_KEY",
        "consumer_secret"     : "REPLACE_THIS_WITH_YOUR_CONSUMER_SECRET",
        "access_token"        : "REPLACE_THIS_WITH_YOUR_ACCESS_TOKEN",
        "access_token_secret" : "REPLACE_THIS_WITH_YOUR_ACCESS_TOKEN_SECRET"
    }
 
    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)

    res = f"A new question on {data['title']} has been posted on tezos stack exchange. Read question here -> {data['link']}."
 
    tweet = res
    status = api.update_status(status=tweet)

if "items" not in questions or len(questions["items"]) == 0:
    print("No new questions found!")
else:
    for data in questions["items"]:
        tweet_question(data)

last_time = int(time.time())

with open("lasttime.txt", "w") as f:
    f.write(str(last_time))
