#!/usr/bin/python3
"""
This module defines the top_ten function that prints the titles
of the first 10 hot posts for a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:sub.topten:v1.0 (by /u/yourusername)'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headparams, allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print("None")
