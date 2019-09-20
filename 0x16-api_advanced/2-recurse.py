#!/usr/bin/python3

from requests import get

"""count number of subscribers"""


def recurse(subreddit, hot_list=[], after=''):
    """Get number of subscribers"""
    endp = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
           subreddit, after)
    header = {'User-Agent': 'RodrigoSV'}
    try:
        allhot = get(endp, headers=header, allow_redirects=False).json()
        for i in allhot['data']['children']:
            hot_list.append(i['data']['title'])
        nextpage = allhot['data']['after']
        if nextpage:
            recurse(subreddit, hot_list, nextpage)
        return hot_list
    except:
        return None
