#!/usr/bin/python3
"""
100-count.py
------------

This module contains a function `count_words` that retrieves all hot posts for
a given subreddit from the Reddit API and counts the occurrences of specified
words in the post titles.

The function sends a GET request to the Reddit API and parses the JSON
response to extract the titles of the hot posts. It then checks each title
for the presence of each word in the provided word list, counting the
occurrences. The function handles potential errors such as non-200 status
codes and JSON decoding errors, returning None in these cases. The function
is recursive, and will continue to retrieve posts until there are no more
to retrieve.
"""
import re
import requests

static_counter = {}

def count_words(subreddit, word_list, after='', count=0):
    """
    This function retrieves all hot posts for a given subreddit and counts the
    occurrences of words in the post titles.

    Parameters:
    subreddit (str): The name of the subreddit to retrieve the hot posts for.
    word_list (list): A list of words to count in the post titles.
    after (str, optional): The ID of the last post in the previous batch.
    Defaults to an empty string.
    count (int, optional): The number of posts retrieved so far. Defaults to 0.

    Returns:
    dict: A dictionary with the words as keys and their counts as values,
    sorted by count in descending order and then alphabetically in ascending
    order. If the subreddit does not exist or an error occurs, it returns None.

    Usage:
    >>> count_words('python', ['python', 'java'])
    {'python': 10, 'java': 5}
    """
    global static_counter

    if not static_counter:
        static_counter = {word.lower(): 0 for word in word_list}

    headers = {'User-Agent': '100-count.py ALX task'}
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
        for title in word_list:
            if re.search(
                r'\b' + re.escape(title) + r'\b',
                post.get('data', {}).get('title', ''),
                re.IGNORECASE
                ):

                static_counter.update({title.lower(): static_counter[title.lower()] + 1})

    after = jsonResp.get('data', {}).get('after', None)
    count += jsonResp.get('data', {}).get('dist', 0)

    if not after:
        results = dict(sorted(static_counter.items(), key=lambda item: (-item[1], item[0])))
        [
            print(f'{key}:', value) for key, value in results.items() if value > 0
        ]
        return results
    else:
        return count_words(subreddit, word_list, after, count)
