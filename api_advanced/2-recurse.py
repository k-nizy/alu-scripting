#!/usr/bin/python3
"""
This module defines the recurse function which recursively queries
the Reddit API and returns a list of titles for all hot posts
in a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves all hot post titles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List of titles accumulated (default: []).
        after (str): ID of the next page to fetch (default: None).

    Returns:
        list or None: List of titles, or None if invalid subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:sub.recurse:v1.0 (by /u/yourusername)'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))

        next_after = data.get("after")
        if next_after is not None:
            return recurse(subreddit, hot_list, next_after)
        return hot_list

    except Exception:
        return None
