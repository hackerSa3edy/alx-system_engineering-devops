#!/usr/bin/python3
"""
This module contains a function `recurse` that retrieves all hot posts for a
given subreddit from the Reddit API.

The function sends a GET request to the Reddit API and parses the JSON
response to extract the titles of the hot posts. It handles potential errors
such as non-200 status codes and JSON decoding errors, returning None in these
cases. The function is recursive, and will continue to retrieve posts until
there are no more to retrieve.
"""
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """
    This function retrieves all hot posts for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to retrieve the hot posts for.
    hot_list (list, optional): A list to store the titles of the hot posts.
    Defaults to an empty list.
    after (str, optional): The ID of the last post in the previous batch.
    Defaults to an empty string.
    count (int, optional): The number of posts retrieved so far. Defaults to 0.

    Returns:
    list: A list of the titles of the hot posts, or None if the subreddit does
    not exist or an error occurs.

    Usage:
    >>> recurse('python')
    ['Post 1 title', 'Post 2 title', ..., 'Post N title']
    """
    headers = {'User-Agent': '2-recurse.py ALX task'}
    params = {'limit': 100, 'after': after, 'count': count}

    resp = requests.get(
        f'https://www.reddit.com/r/{subreddit}/hot.json',
        params=params,
        headers=headers,
        allow_redirects=False
        )

    if resp.status_code != 200:
        return None

    try:
        jsonResp = resp.json()
    except requests.exceptions.JSONDecodeError:
        return None

    for post in jsonResp.get('data', {}).get('children', {}):
        title = post.get('data', {}).get('title', {})
        hot_list.append(title)

    after = jsonResp.get('data', {}).get('after', None)
    count += jsonResp.get('data', {}).get('dist', 0)
    if not after:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after=after, count=count)
