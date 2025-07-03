#!/usr/bin/python3
"""
This module defines a recursive function that queries the Reddit API,
parses all hot article titles of a subreddit, and counts keyword
occurrences from a given list.
"""

import re
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries Reddit API, parses hot article titles,
    and counts the occurrences of words from a list.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): Pagination parameter (for recursion).
        word_count (dict): Dictionary tracking keyword counts.

    Returns:
        None
    """
    if not word_count:
        # Initialize dictionary with lowercase deduplicated keys
        for word in word_list:
            key = word.lower()
            word_count[key] = word_count.get(key, 0)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:word.counter:v1.0 (by /u/yourusername)'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title", "")
            # Match words using regex to avoid punctuation issues
            words = re.findall(r'\b\w+\b', title.lower())
            for w in words:
                if w in word_count:
                    word_count[w] += 1

        if data.get("after"):
            return count_w(subreddit, word_list, data.get("after"), word_count)

        # Only print once recursion ends
        sorted_words = sorted(
            [(k, v) for k, v in word_count.items() if v > 0],
            key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_words:
            print(f"{word}: {count}")

    except Exception:
        return
