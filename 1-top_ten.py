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
    for post in response.json().get("data").get("children"):
        print(post.get("data").get("title"))
        
    