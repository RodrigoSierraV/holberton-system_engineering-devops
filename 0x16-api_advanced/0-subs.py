#!/usr/bin/python3

from requests import get

"""count number of subscribers"""


def number_of_subscribers(subreddit):
    """Get number of subscribers"""
    endp = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'RodrigoSV'}
    try:
        subscribers = get(endp, headers=header, allow_redirects=False)
        return subscribers.json()['data']['subscribers']
    except:
        return 0
