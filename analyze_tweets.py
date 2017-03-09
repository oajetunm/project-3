#analyze_tweets.py

import sqlite3 

conn = sqlite3.connect('tweets.db')


print('***** MOST FREQUENTLY MENTIONED AUTHORS *****')

# Print the 5 most frequently mentioned authors in the entire corpus

print('*' * 20, '\n\n') # dividing line for readable output



print('***** TWEETS MENTIONING AADL *****')

# Print all tweets that mention the twitter user 'aadl' (the Ann Arbor District Library)

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