from cPickle import load
import sys

from pymongo import MongoClient
import tweepy

# Get access keys from pickle file in local memory
# Insert proper consumer and keys and access tokens
access_keys = load(file('twitter_access.pkl'))

consumer_key = access_keys['api_key']
consumer_secret = access_keys['api_secret']
access_token = access_keys['access_token']
access_token_secret = access_keys['access_secret']


class MongoStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.

        This listener that takes the received tweets and stores them in a
        NoSQL MongoDB database.

    """
    def __init__(self, api, db):
        super(tweepy.StreamListener, self).__init__()
        self.api = api
        self.db = db

    def on_status(self, status):
        print status.place, "\n"

        data = {'text': status.text,
                'created_at': status.created_at,
                'coordinates': status.coordinates,
                'source': status.source}

        self.db.tweets.insert(data)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True  # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True  # Don't kill the stream

if __name__ == '__main__':
    # Connect to Twitter streaming API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # Connect to MongoDB database
    db = MongoClient().cl
    # Instantiate MongoStreamListener and pass it as argument to the Stream
    sapi = tweepy.streaming.Stream(auth, MongoStreamListener(api, db))
    # Filter tweets according to a specified list of words to track
    sapi.filter(track=['afc', 'arsenal', 'bvb', 'afcbvb', 'borussia'])
