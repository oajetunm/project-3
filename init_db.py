#init_db.py

import sqlite3
import tweepy
from tweepy import OAuthHandler
import json
import time
from collections import Counter



conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tweets')
cur.execute('CREATE TABLE Tweets (author_id INT,time_stamp TEXT, tweet_id INT,tweet TEXT )')

cur.execute('DROP TABLE IF EXISTS Mentions')
cur.execute('CREATE TABLE Mentions (tweet_id INT, author_id INT )')
#
cur.execute('DROP TABLE IF EXISTS Authors')
cur.execute('CREATE TABLE Authors (author_id INT, username TEXT)')

CONSUMER_KEY = "SGS9ZMk1h0CvkfVJ6uvFZiZfv"
CONSUMER_SECRET = "BEcNaMbQbaG7oDoZKT2yztyYa0haJwlqmz8SYr0O5CBa3zIhIf" 		# enter your consumer secret
ACCESS_TOKEN = "212920273-pjmAKzWw23rkLinFFNfJE9A96uE4F2qB3wr1vr7n"			# enter your access token
ACCESS_TOKEN_SECRET = "wBsz1Ze4xOAtNTWelk0NJcyI2GRnEK77qcWNwK1A4jyvy"

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# with open('umsitweets.json', 'w') as json_file:
#     for status in tweepy.Cursor(api.user_timeline, screen_name = '@umsi').items():
#         g  = status._json
#         json_file.write(json.dumps(g))
#         json_file.write('\n')
lst_name = []
lst_author = []
count = []
tweet_id = []
with open('umsitweets.json', 'r') as json_file:
    for i in json_file:
        data = json.loads(i)

        date = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
        if date > '2016-09-01 00:00':
            users = data['entities']['user_mentions']
            tweet_id = data['id']
            for item in users:
                author_id = item['id']
                cur.execute('INSERT INTO Mentions(tweet_id, author_id) VALUES (?,?)',
                    ((tweet_id, author_id)))



            cur.execute('INSERT INTO Tweets(author_id , time_stamp, tweet_id,tweet) VALUES (?,?,?,?)',
                ((data['user']['id'], date ,data['id'],data['text'])))
            conn.commit()
            for each in (data['entities']['user_mentions']):
                x = each.get('screen_name', None)
                print(x)


                if x not in lst_name:
                    lst_name.append(x)
                    continue
            for each in (data['entities']['user_mentions']):
                x = each.get('id', None)
                if x not in lst_author:
                    lst_author.append(x)

#print (tweet_id)
author_info = list(zip(lst_author, lst_name))
tabl_auth = 'INSERT INTO Authors VALUES (?,?)'
for item in author_info:
     cur.execute(tabl_auth, item)
conn.commit()

# mentions_auth = 'INSERT INTO Mentions VALUES (?,?)'
# for item in tweet_id:
#     cur.execute(mentions_auth, item)
# conn.commit()




# top_neighbors = items[1:20]
# neighbors = [j[1] for j in top_neighbors]
#
# with open('tweets.json', 'w') as json_file:
#     for m in range(19):
#         for status in tweepy.Cursor(api.user_timeline, screen_name = neighbors[m]).items(20):
#             g  = status._json
#             date2 = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(g['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
#
#             if date2 > '2016-09-01 00:00':
#
#                 json_file.write(json.dumps(g))
#                 json_file.write('\n')

#print(neighbors)
lst_name2 =[]
lst_author2 = []
with open('tweets.json', 'r') as json_file:
    for i in json_file:
        data2 = json.loads(i)
        date2 = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(data2['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
        users = data2['entities']['user_mentions']
        tweet_id = data2['id']
        for item in users:
            author_id = item['id']
            cur.execute('INSERT INTO Mentions(tweet_id, author_id) VALUES (?,?)',
                ((tweet_id, author_id)))



        cur.execute('INSERT INTO Tweets(author_id , time_stamp, tweet_id,tweet) VALUES (?,?,?,?)',
            ((data2['user']['id'], date2 ,data2['id'],data2['text'])))
        conn.commit()


        for each in (data2['entities']['user_mentions']):
            x = each.get('screen_name', None)




            if x not in lst_name:
                if x not in lst_name2:
                    lst_name2.append(x)
                    continue
        for each in (data2['entities']['user_mentions']):
            x = each.get('id', None)
            if x not in lst_author:
                if x not in lst_author2:
                    lst_author2.append(x)
                    continue


author_info2 = list(zip(lst_author2, lst_name2))
tabl_auth2 = 'INSERT INTO Authors VALUES (?,?)'
for item in author_info2:
 cur.execute(tabl_auth2, item)
conn.commit()





# Put code here to create the database and tables
#
# You may want to set this up so that you can also DROP or TRUNCATE tables
# as you are developing so that you can start from scratch when you need to
# counter_dict = Counter(count)
# print (counter_dict)
# items = [(v,k) for k,v in counter_dict.items()]
# items.sort()
# items.reverse()

conn.close()
