#credited to professor's example
import redis
import time

conn = redis.Redis()  # build redis connection

while True:

    locations = conn.keys()  #extract all keys from redis
    
    for location in locations:  #tranverse all loaction

        d = conn.hgetall(location)   #get the infomation of source and number
        
        for src in d:          #if number is greater than 1, then subtract 1
            if int(d[src]) > 1:
                count = int(d[src])
                count -= 1
                d[src] = str(count)
        conn.hmset(location,d)

    time.sleep(3)


