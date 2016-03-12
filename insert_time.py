import json
import sys
import redis
import time



while 1:
    line = sys.stdin.readline()
    try:
        d = json.loads(line)
    except ValueError:
        # if  we get an empty line, we will skip that
        continue

    try:
        location = d["lo"]
    except KeyError:
        # if there is no location information in our message
        # then we store a "null" 
        location = "null"

    t = str(time.time())
    
    print json.dumps({"t":t, "lo":location})
    sys.stdout.flush()
