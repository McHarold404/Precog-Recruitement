import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = "ASNOVzBKLfvz5gNtspT3eVAGR"
consumer_secret = "LgbZmaxsfVbMmdnCzvTjROviS2VhpKtWWM8XxyEEokQucg0BvQ"
    #access_key = "ASNOVzBKLfvz5gNtspT3eVAGR"
    #access_secret = "LgbZmaxsfVbMmdnCzvTjROviS2VhpKtWWM8XxyEEokQucg0BvQ"
access_token = "1340389657268289536-QvI1MhyGj8LA1yjapll16TwbA3d1kA"
access_token_secret = "65rkBEfxpB9DMxIXPdbkzBon4kQlBeOHQkGrncYnVmkTp"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#MUFC",count=3200,lang="en",since="2017-04-03").items():
    #try:
    print(type(tweet.user))
    print (tweet.created_at, tweet.user.id, tweet.entities.get('hashtags'), tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.user.id,tweet.user.name,tweet.user.location,tweet.user.protected,tweet.user.followers_count,tweet.user.friends_count, tweet.text.encode('utf-8')])
    