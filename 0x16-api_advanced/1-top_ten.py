#!/usr/bin/python3
"""Module for top_ten()."""
import json
import requests


def top_ten(subreddit):
    """"prints the titles of 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)

    response = requests.get(url, headers={'User-agent': 'MyLinuxApp/1.0'},
                            allow_redirects=False)
    if response.status_code == 404:
        print(None)
    data = json.loads(response.text).get('data', {}).get('children', [])
    for post in data:
        title = post.get('data', {}).get('title')
        print(title)
