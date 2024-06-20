#!/usr/bin/python3
"""
This module contains a function `number_of_subscribers` that retrieves the
number of subscribers for a given subreddit from the Reddit API.

The function sends a GET request to the Reddit API and parses the JSON
response to extract the number of subscribers. It handles potential errors
such as non-200 status codes and JSON decoding errors, returning 0 in
these cases.
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function retrieves the number of subscribers for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to retrieve the subscriber
    count for.

    Returns:
    int: The number of subscribers for the subreddit. If the subreddit does
    not exist or an error occurs, it returns 0.

    Usage:
    >>> number_of_subscribers('python')
    2345678
    """

    headers = {'User-Agent': '0-subs.py ALX task'}

    resp = requests.get(
        f'https://www.reddit.com/r/{subreddit}/about.json',
        headers=headers,
        allow_redirects=False
        )

    if resp.status_code != 200:
        return 0

    try:
        jsonResp = resp.json()
    except requests.exceptions.JSONDecodeError:
        return 0

    subscribers = jsonResp.get('data', {}).get('subscribers', 0)
    return subscribers
