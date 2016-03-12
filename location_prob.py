# credited to professor's slides and example

import flask
from flask import request
import redis
import collections
import json
import numpy as np

app = flask.Flask(__name__)
conn = redis.Redis()
conn2 = redis.Redis(db=2)  # call the second connection
#this function is to obtain distribution of source
def buildHistogram():
    keys = conn.keys()
    values=[]
    for key in keys:
      values.append(conn.hgetall(key).keys()[0])  #store all url address into values list
    #print values
    c = collections.Counter(values)     # integrate url address, which is a dict incluing url and its count
    z = sum(c.values())
    return {k:v/float(z) for k,v in c.items()}   #calculate its precentage
def frate():
    key = conn2.keys()       #get location
    value = conn2.mget(key)   #get rate
    return value
@app.route("/")
def histogram():
    h = buildHistogram()
    return json.dumps(h)
    

@app.route("/rate")
def showrate():
    rate = frate()
    #return json.dumps(rate)
    if float(rate[0]) > 0.05:
      return json.dumps({"rate":"abnormal rate"})
    #else:
    return json.dumps({"rate":rate[0]})
# this function is to calculate entropy value
@app.route("/entropy")
def entropy():
    h = buildHistogram()
    sum=0
    
    for p in h.values():
      #p2=round(p,4) if we want to round off, we can use this code
      a = np.log(p)
      sum = sum + p*a
    return json.dumps(-sum)
    #return -sum([p*np.log(p) for p in h.values()]) 

# this function is to calculate the probability of source url address from the same location.
@app.route("/probability")
def probability():
    location = request.args.get('location','')
    src = request.args.get('source','')
    # extract loaction and source info from url
    
    d = conn.hgetall(location)  # get the count and web infomation
    #print d
    # get the count for the url address
    try:
      		c = d[src]
    except KeyError:
      		return json.dumps({
        	"location": location, 
        	"prob": 0,
        	"source": src
      		})
    # we will obtain the normalising constant
    print d.values()

    z = sum([float(v) for v in d.values()])
    return json.dumps({
      "location": location, 
      "prob": float(c) / z,
      "source": src
      })

 


if __name__ == "__main__":
    app.debug = True
    app.run()
