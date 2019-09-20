#!/usr/bin/python3

from requests import get

"""count number of subscribers"""


def top_ten(subreddit):
    """Get number of subscribers"""
    endp = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'RodrigoSV'}
    try:
        top10 = get(endp, headers=header, allow_redirects=False,
                    params={'limit': 10})
        for i in top10.json()['data']['children']:
            print(i['data']['title'])
    except:
        print(None)
