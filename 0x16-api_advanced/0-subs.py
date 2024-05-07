#!/usr/bin/python3
"""A funcrion that queries the Reddit API and returns the number of subscribers
for a given subreddit."""

import requests
import json


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/requests'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
