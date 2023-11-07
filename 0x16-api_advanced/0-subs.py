#!/usr/bin/python3
"""Module for number_of_subscribers()."""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Return total number of subscribers for a given subredit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers={'User-agent': 'MyLinuxApp/1.0'},
                            allow_redirects=False)
    if response.status_code == 404:
        return 0
    response = response.json()
    subscribers = response.get('data').get('subscribers')
    return subscribers
