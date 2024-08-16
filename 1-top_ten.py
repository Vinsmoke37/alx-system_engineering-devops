#!/usr/bin/python3
"""Top Ten"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(None)
        return       
    data = response.json()
    for post in data["data"]["children"]:
        print(post["data"]["title"])