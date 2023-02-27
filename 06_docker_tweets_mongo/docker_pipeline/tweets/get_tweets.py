#Loading Scripts and Libraries
from credentials import *
import tweepy
import logging
import pymongo

##### AUTHENTICATION #####

client = tweepy.Client(  bearer_token        = BEARER_TOKEN
                      #, consumer_key        = API_KEY
                      #, consumer_secret     = API_KEY_SECRET
                       , access_token        = API_KEY
                       , access_token_secret = API_KEY_SECRET )
+++
if client:
    logging.critical("\nAutentication OK")
else:
    logging.critical('\nVerify your credentials')


# remove evrything from the collection tweets_gazprom



# Define a search string
# query = "gazprom"
query = "gazprom pipeline baltic"



#look for this search string
search_gazprom = client.search_recent_tweets(query=query, 
                                                                                 tweet_fields=['id','created_at','text','conversation_id','referenced_tweets'],
                                                                                 max_results=10)

#Connect to MongoDB
client = pymongo.MongoClient(host="mongodb", port=27017)
client.drop_database('twitter')
db = client.twitter

#Create result and table list
result_list=[search_gazprom]
table_list=["tweets_gazprom"]
for result in result_list:
    for tweet in result.data:
        logging.critical(f'\n\n\nINCOMING TWEET:\n{tweet.text}\n\n{tweet.created_at}\n')
        index=result_list.index(result)
        table_name=table_list[index]
        #print(index)
        db[table_name].insert_one(dict(tweet))
