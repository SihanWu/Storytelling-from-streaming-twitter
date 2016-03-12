#!/usr/bin/python
#the function of this program is to obtain the location and referrer infomation of sentences 
#which contain "python" or "streaming" or "java" in tweets
#Import the necessary methods from tweepy library

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import pandas as pd
import re
import time
from sys import stdout
import urlparse


#Variables that contains the user credentials to access Twitter API 
access_token = "3527076748-HflTXP74NjSWDIyuAmakc69VqTAZ29WIUVfdgjE"
access_token_secret = "XSKSRbfQ2baQFJ5Sc9WrSPf6AT05NvdpMtQi6fGLajEoR"
consumer_key = "X8B3WiESc1q6v8NQqRcP3kUvw"
consumer_secret = "Wb619BUbvSOTZ3Azoe1oYkCmVRE7yD3TkZMjFobDoi64XEcCLX"
#input kinds of secert key
def count_number(file):    #define a function which can get the number of sentences including specific keyword and print them on screen
    tweets_data = []
    tweets_file = open(file, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            o = urlparse.urlparse(tweet["user"]["url"])
            url = o.netloc
            
            if tweet["user"]["location"]=="null":
                continue
            print json.dumps({"location":tweet["user"]["location"],"source":url})
            sys.stdout.flush()
            
            #time.sleep(3)
            
        except:
            continue

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            savefile=open('data.csv','a') #open file data.csv
            savefile.write(data)
            savefile.write('\n') # store tweets in file
            savefile.close()
            count_number('data.csv')
            time.sleep(3)
            return True
        except:
            print "erroropen"
    def on_error(self, status):
        print status

#This handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=['python', 'java', 'streaming'])
#This line filter Twitter Streams to capture data by the keywords: 'python', 'java','streaming'
