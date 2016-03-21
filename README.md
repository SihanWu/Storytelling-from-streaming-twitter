# track_tweet_and_api

### 1.Build a system to track a distrbution or set of distributions that capture something you find interesting about a stream of data. (40%)

Inspired by professor's example:citibike. I decided to utilize twitter streaming api, and single information twitter api returns is something like this:

{"created_at":"Fri Mar 04 18:50:42 +0000 2016","id":705827827896156160,"id_str":"705827827896156160","text":"RT @AppStore: Knock, knock. @HouseofCards Season 4 is now streaming on @Netflix. https:\/\/t.co\/Ce7EJjhZkT https:\/\/t.co\/MiV3442vRj","source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":2168159444,"id_str":"2168159444","name":"Gareth Smith","screen_name":"gxz_smith","location":null,"url":"http:\/\/Instagram.com\/gxz_smith","description":"\u27b018\u27b0snapchat - sheep444 #justinbieber","protected":false,"verified":false,"followers_count":405,"friends_count":490,"listed_count":5,"favourites_count":2165,"statuses_count":1725,"created_at":"Fri Nov 01 10:03:51 +0000 2013","utc_offset":0,"time_zone":"Dublin","geo_enabled":true,"lang":"en-gb","contributors_enabled":false,"is_translator":false,"profile_background_color":"000000","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"9266CC","profile_sidebar_border_color":"000000","profile_sidebar_fill_color":"000000","profile_text_color":"000000","profile_use_background_image":false,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/666999725422419968\/S2MmFj73_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/666999725422419968\/S2MmFj73_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/2168159444\/1449433430","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweeted_status":{"created_at":"Fri Mar 04 17:15:42 +0000 2016","id":705803919847399425,"id_str":"705803919847399425","text":"Knock, knock. @HouseofCards Season 4 is now streaming on @Netflix. https:\/\/t.co\/Ce7EJjhZkT https:\/\/t.co\/MiV3442vRj","source":"\u003ca href=\"http:\/\/twitter.com\" rel=\"nofollow\"\u003eTwitter Web } (it's not all of it and i only show some of it to explain what i received)


It includes too much information, to simplify, I decided to keep track of the location and source infomation(url) of tweets which includes "python" or"java" or "streaming" in their sentences, so i used :


            tweet = json.loads(line)
            o = urlparse.urlparse(tweet["user"]["url"])
            url = o.netloc
            if tweet["user"]["location"]=="null":
                continue
            print json.dumps({"location":tweet["user"]["location"],"source":url})
            sys.stdout.flush()
            
to extract location and source url information from what api returns.
And this is the function of program twtw.py. And then i used insert.py to insert location by source, put them in conn1, and print out on terminal. So here, i completed the task of building a system to track a distrbution. The detailed processing is in api part.

### 2. Build an API (40%) that can return:

the rate of the stream
the distributions you assembled in the first part of this exercise
the entropy of the distributions
the probability of a new message given the stored distributions

(1)Next, i used insert_time.py to obtain rate based on location. After that,  i wrote calrate.py to calculate rate, which is time interval between two messages.
At the same time, i open a new terminal winodw to run decrementer.py to subtract source number.(similar to referrer number
in professor's example.)
(2) after extracting data from conn and processing, i got the distributions for every location and url 
(3)Through the entrophy formula and data we got from streaming, i calculated entrophy value.
(4)By the @app.route("/probability") part, i extracted information in url and calculated probability of specific url website in specific location.

Finally, i wrote location_prob.py to create an api, which includes the following functions:

1. http://127.0.0.1:5000                   show all distribution based on location and source url 

2. http://127.0.0.1:5000/entropy           show the entropy of information

3. http://127.0.0.1:5000/probability?location=(fill out the location name you want to see)&source=(url address)
for example, i want to see the probability of facebook address in London. Then i can input
http://127.0.0.1:5000/probability?location=London&source=www.facebook.com
then i can see result like {"source": "www.facebook.com", "location": "London", "prob": 0.014492753623188406}

4. http://127.0.0.1:5000/rate             show the rate of message and when rate is greater than 0.05s then something 
serious must happen and webpage will show "abnormal rate" because normal rate in my program should be about 0.005s(that's alert system)


### 3.Extend the alerting system you built in Exercise 2 to alert on changes in entropy or unlikey new messages. (10%)
@app.route("/rate")
def showrate():
    rate = frate()
    #return json.dumps(rate)
    if float(rate[0]) > 0.05:
      return json.dumps({"rate":"abnormal rate"})
    #else:
    return json.dumps({"rate":rate[0]})
the code above shows if rate is greater than 0.05s then something serious must happen and webpage will show "abnormal rate" because normal rate in my program should be about 0.005s after my design and multiple tests.

### 4. Build a webpage that displays the current distribution(s) stored in your system by querying the API you build in the second part of this exercise. (10%)

Like what i showed in previous part, after we run location_prob.py in terminal, we can input these urls to show function.

1. http://127.0.0.1:5000                   show all distribution based on location and source url 

2. http://127.0.0.1:5000/entropy           show the entropy of information

3. http://127.0.0.1:5000/probability?location=(fill out the location name you want to see)&source=(url address)
for example, i want to see the probability of facebook address in London. Then i can input
http://127.0.0.1:5000/probability?location=London&source=www.facebook.com
then i can see result like {"source": "www.facebook.com", "location": "London", "prob": 0.014492753623188406}

4. http://127.0.0.1:5000/rate             show the rate of message and when rate is greater than 0.05s then something 
serious must happen and webpage will show "abnormal rate" because normal rate in my program should be about 0.005s(that's alert system)
