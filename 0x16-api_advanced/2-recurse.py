#!/usr/bin/python3
"""Module for top_ten()."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """prints the titles of 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/top.json?after={}".format(subreddit, after)

    response = requests.get(url, headers={'User-agent': 'MyLinuxApp/1.0'},
                            allow_redirects=False)
    if response.status_code >= 300:
        return None

    data = response.json().get('data').get('children')
    for post in data:
        title = post.get('data').get('title')
        hot_list.append(title)
    after = response.json().get('data').get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
