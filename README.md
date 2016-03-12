# track_tweet_and_api

Basing on twitter streaming api, I keep track of the location and source infomation of tweets which includes "python" or
"java" or "streaming" in their sentences, which is the function of program twtw.py.

And then i used insert.py to insert location by source, put them in conn1, and print out on terminal.

Next, i used insert_time.py to obtain rate based on location. After that,  i wrote calrate.py to calculate rate, which is
time interval between two messages.

At the same time, i open a new terminal winodw to run decrementer.py to subtract source number.(similar to referrer number
in professor's example.)

Finally, i wrote location_prob.py to create an api, which includes the following functions:

1. http://127.0.0.1:5000                   show all distribution based on location and source url 

2. http://127.0.0.1:5000/entropy           show the entropy of information

3. http://127.0.0.1:5000/probability?location=(fill out the location name you want to see)&source=(url address)
for example, i want to see the probability of facebook address in London. Then i can input
http://127.0.0.1:5000/probability?location=London&source=www.facebook.com
then i can see result like {"source": "www.facebook.com", "location": "London", "prob": 0.014492753623188406}

4. http://127.0.0.1:5000/rate             show the rate of message and when rate is greater than 0.05s then something 
serious must happen and webpage will show "abnormal rate" because normal rate in my program should be about 0.005s(that's alert system)
