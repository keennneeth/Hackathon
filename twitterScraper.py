import tweepy
import webbrowser
import time

consumer_key = "9EtOt0yxbLXMcacXqq3ZXa9DW"
consumer_secret = "znnM11aWMVBaGhDavdTei0qGPCzsdUT2gySSXkUXGBB2mklrPm"
access_token = "1497611724165427203-2bJbh949PAEf4po4otegcMHcUca7OF"
access_token_secret = "4B3yF2PEWXUtE0YQKzJK3DM0P8lsRhsOtURnmt4LRhXWb"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")

#test