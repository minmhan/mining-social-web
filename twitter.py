# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 20:32:20 2016

@author: minmhan
"""

import twitter
import json

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_OAUTH_TOKEN = ''
TWITTER_OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

def trend():
    WORLD_WOE_ID = 1
    US_WOE_ID = 23424977
    
    world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
    us_trends = twitter_api.trends.place(_id=US_WOE_ID)
    
    world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
    us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']])
    common_trends = world_trends_set.intersection(us_trends_set)
    
    print(common_trends)

def search(q='#ShawnMendesTODAY'):
    count = 100
    search_results = twitter_api.search.tweets(q=q, count=count)
    status = search_results['statuses']
    
    for _ in range(5):
        print('Length of statuses', len(status))
        try:
            next_results = search_results['search_metadata']['next_results']
        except:
            break
        
        kwargs = dict([kv.split('=') for kv in next_results[1:].split('&')])
        search_results = twitter_api.search.tweets(**kwargs)
        status += search_results['statuses']
        
    print(json.dumps(status[0], indent=1))
    
search()