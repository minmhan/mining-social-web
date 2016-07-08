# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 22:36:44 2016

@author: minmhan
"""
import os
import json
import requests
from github import Github

ACCESS_TOKEN = os.environ.get('GITHUB_PERSONAL_API_TOKEN')

def access():
    url = 'https://api.github.com/repos/ptwobrussell/Mining-the-Social-Web/stargazers'
    response = requests.get(url)
    
    print(json.dumps(response.json()[0], indent=1))
    for (k,v) in response.headers.items():
        print(k,"=>",v)
        

def stargazers(user='ptwobrussell', repo='Mining-the-Social-Web'):
    client = Github(ACCESS_TOKEN, per_page=100)
    user = client.get_user(user)
    repo = user.get_repo(repo)
    
    stargazers = [s for s in repo.get_stargazers()]
    print("number of stargazers: ", len(stargazers))
    
stargazers()