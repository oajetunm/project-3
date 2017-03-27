#analyze_tweets.py

import sqlite3

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

# Print the 10 most common verbs ('VB' in the default NLTK part of speech tagger)
# that appear in tweets from the umsi account

print('*' * 20, '\n\n')



print('***** MOST COMMON VERBS IN UMSI "NEIGHBOR" TWEETS *****')

# Print the 10 most common verbs ('VB' in the default NLTK part of speech tagger)
# that appear in tweets from umsi's "neighbors", giving preference to tweets from
# umsi's most "mentioned" accounts

print('*' * 20, '\n\n')


conn.close()
