import json
import sys  #import kinds of libraries
import redis

lastime = 0   #set lastime=0
interval_list=[]
conn2 = redis.Redis(db=2)
while 1:
    line = sys.stdin.readline()  #read every line in standard in and reference to line
    d = json.loads(line)    #transform line into json format so that to print out
    if lastime == 0 :       # if this is the first time dectection
        try:
        	lastime = float(d["t"])    #  then make lastime equals the value of time and start next loop
        except:
        	continue
    print d["t"]
    time_interval = float(float(d["t"])-lastime )  # calculate time interval
    interval_list.append(time_interval)
    if len(interval_list):   #if the length of intervals is greater than 0
            rate = sum(interval_list)/float(len(interval_list))   #rate equals summation divided by the length
    lastime = float(d["t"]) #make lastime value equals the time now  
            
    print json.dumps({"rate":rate})  #transform data into json for output
    sys.stdout.flush()
    
    conn2.setex("rate",rate,300)    # put rate information into connection for 300 seconds


