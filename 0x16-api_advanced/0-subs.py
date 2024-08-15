#!/usr/bin/python3

import requests

headers = {"User-Agent": "user_agent_text"}


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url,allow_redirects=False,headers=headers)
    if response.status_code != 200:
        return 0
    return response.json().get("data").get("subscribers")


