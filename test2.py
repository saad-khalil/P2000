from eca import *
from eca.generators import start_offline_tweets
import datetime
import textwrap

@event('init')
def setup(ctx, e):
    start_offline_tweets('data/p2000.txt', event_name='chirp', time_factor=10000)

@event('chirp')
def tweet(ctx, e):
    tweet = e.data
    text= tweet['text']
    emit('tweet', text)
