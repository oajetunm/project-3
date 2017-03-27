#analyze_tweets.py

import sqlite3
import nltk
from collections import Counter

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

print('***** MOST FREQUENTLY MENTIONED AUTHORS *****')

# Print the 5 most frequently mentioned authors in the entire corpus
x = cur.execute('SELECT Authors.username, COUNT(*) FROM Mentions JOIN Authors ON Authors.author_id = Mentions.author_id GROUP BY Mentions.author_id ORDER BY COUNT(*) DESC LIMIT 10')
for g in x:
    print(g)

print('*' * 20, '\n\n') # dividing line for readable output



print('***** TWEETS MENTIONING AADL *****')

# Print all tweets that mention the twitter user 'aadl' (the Ann Arbor District Library)
g = cur.execute('SELECT Tweets.tweet, Tweets.time_stamp FROM Tweets JOIN Mentions  ON Mentions.tweet_id  = Tweets.tweet_id JOIN Authors ON Authors.author_id = Mentions.author_id WHERE username="aadl"')
for t in g:
    print(t)
print('*' * 20, '\n\n')



print('***** MOST COMMON VERBS IN UMSI TWEETS *****')

token_lst = []
top = []
f = cur.execute('SELECT Tweets.tweet FROM Tweets JOIN Authors on Authors.author_id = Tweets.author_id Where username = "umsi"')
for x in f:
    tokens = nltk.word_tokenize(x[0])
    n = nltk.pos_tag(tokens)
    #print(n)
    no_lst = ['@', '-', '_', b'\xe2\x80\xa6'.decode(), 'umsi', 'umsiasb17', 'umich', 'https']

    for thing in n:
        if thing[1] == 'VB':
            if thing[0] not in no_lst:
                token_lst.append(thing[0])



            # print(token_lst)
    count_dict = Counter(token_lst)
    dict_items = count_dict.items()
    new_lis = sorted(dict_items, key = lambda x :x[1], reverse = True)[:10]
    #print(new_lis)
for each in new_lis:
    print('{} ({} times)'.format(each[0], each[1]))

        #print('{} {}'.format(new_lis[i][0], new_lis[i][1]))




# Print the 10 most common verbs ('VB' in the default NLTK part of speech tagger)
# that appear in tweets from the umsi account

print('*' * 20, '\n\n')



print('***** MOST COMMON VERBS IN UMSI "NEIGHBOR" TWEETS *****')

# Print the 10 most common verbs ('VB' in the default NLTK part of speech tagger)
# that appear in tweets from umsi's "neighbors", giving preference to tweets from
# umsi's most "mentioned" accounts
token_lst2 = []

top = []
f = cur.execute('SELECT Tweets.tweet FROM Tweets JOIN Authors on Authors.author_id = Tweets.author_id Where username != "umsi"')
for x in f:
    tokens = nltk.word_tokenize(x[0])
    n = nltk.pos_tag(tokens)
    #print(n)
    no_lst = ['@', '-', '_', b'\xe2\x80\xa6'.decode(), 'umsi', 'umsiasb17', 'umich', 'https']

    for thing in n:
        if thing[1] == 'VB':
            if thing[0] not in no_lst:
                token_lst2.append(thing[0])



            # print(token_lst)
    count_dict = Counter(token_lst2)
    dict_items = count_dict.items()
    new_lis = sorted(dict_items, key = lambda x :x[1], reverse = True)[:10]
    #print(new_lis)
for each in new_lis:
    print('{} ({} times)'.format(each[0], each[1]))

print('*' * 20, '\n\n')


conn.close()
