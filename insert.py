#credited to professor's example 
import json
import sys
import redis
import time
import urlparse

conn = redis.Redis()
#conn2 = redis.Redis()
lastime = 0
rate=0
interval_list=[]
while True:
    line = sys.stdin.readline()

    try:
        d = json.loads(line)
    except ValueError:
        # when we obtain an empty line, then we can just skip it
        continue

    try:
        location = d["location"]
    except KeyError:
        # if there is no location information in our  message
        # then skip
        continue

    try:
        source = d["source"]
    except KeyError:
        # if there is no source url infomation in our message
        # then skip
        continue
    if location == "null" or location == None:
            continue
    
    netloc = source
    conn.hincrby(location, netloc, 1)
    print json.dumps({"lo": location, "s": source})
    sys.stdout.flush()
    
