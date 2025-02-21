#!/usr/bin/python3
"""
Module to interact with the Reddit API and print titles of hot posts.
"""
import requests
import sys

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None. Prints None if the subreddit is invalid or an error occurs.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("None")
            sys.exit(0)

        for post in posts:
            title = post['data']['title']
            print(title)  # Print each title on a new line

    except requests.exceptions.RequestException:
        print("None")
        sys.exit(0)

    except (ValueError, KeyError):
        print("None")
        sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
        sys.exit(1)
    else:
        top_ten(sys.argv[1])
