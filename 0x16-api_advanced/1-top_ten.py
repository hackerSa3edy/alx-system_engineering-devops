#!/usr/bin/python3
"""
This module contains a function `top_ten` that retrieves the top ten hot posts
for a given subreddit from the Reddit API.

The function sends a GET request to the Reddit API and parses the JSON response
to extract the titles of the top ten hot posts. It handles potential errors
such as non-200 status codes and JSON decoding errors, printing 'None'
in these cases.
"""
import requests


def top_ten(subreddit):
    """
    This function retrieves the top ten hot posts for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to retrieve the hot posts for.

    Returns:
    None: This function does not return a value. It prints the titles of the
    top ten hot posts, or 'None' if the subreddit does not exist or
    an error occurs.

    Usage:
    >>> top_ten('python')
    Post 1 title
    Post 2 title
    ...
    Post 10 title
    """
    headers = {'User-Agent': '1-top_ten.py ALX task'}
    params = {'limit': 9}

    resp = requests.get(
        f'https://www.reddit.com/r/{subreddit}/hot.json',
        params=params,
        headers=headers,
        allow_redirects=False
        )

    if resp.status_code != 200:
        print('None')
        return None

    try:
        jsonResp = resp.json()
    except requests.exceptions.JSONDecodeError:
        print('None')
        return None

    for post in jsonResp.get('data', {}).get('children', {}):
        title = post.get('data', {}).get('title', {})
        print(title)
