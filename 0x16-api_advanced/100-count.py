#!/usr/bin/python3
"""Module for count_words()."""
import requests


def count_words(subreddit, word_list, after=None, hots_dict={}):
    """print sorted count of given keywords of hot articles."""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
                subreddit, after)

    response = requests.get(url, headers={'User-agent': 'MyLinuxApp/1.0'},
                            allow_redirects=False)
    if response.status_code >= 300:
        return None

    data = response.json().get('data').get('children')
    after = response.json().get('data').get('after')
    for post in data:
        title = post.get('data').get('title')
        lower_list = [hot.lower() for hot in title.split(' ')]

        for hot in hots_dict.keys():
            hots_dict[hot] += lower_list.count(hot)

    if after is None:
        word_items = hots_dict.items()
        sorted_word_dict = sorted(word_items, key=lambda x: (-x[1], x[0]))

        for word in sorted_word_dict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    if not hots_dict:
        for word in word_list:
            if word.lower() not in hots_dict:
                hots_dict[word.lower()] = 0

    count_words(subreddit, word_list, after, hots_dict)
