#!/usr/bin/python3
"""
Fetches and prints the titles of the first 10 hot posts from a given subreddit.

Functions:
    top_ten(subreddit): Fetches and prints the top 10 hot posts.

Usage:
    Call top_ten("subreddit_name") with a valid subreddit name.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; top_ten_script/1.0)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    posts = response.json().get("data", {}).get("children", [])

    if not posts:
        print("None")
        return

    for post in posts:
        print(post["data"]["title"])

    print("OK")

