#!/usr/bin/python3
"""
Module to query Reddit API and get number of subscribers of a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    Returns 0 if the subreddit is invalid or request fails.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyRedditBot/1.0; +https://github.com/yourusername)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0

