#!/usr/bin/python3
"""
This module interacts with the Reddit API to retrieve and display
the titles of the top 10 hot posts for a given subreddit. It handles
invalid subreddits gracefully by printing "None".
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
    headers = {'User-Agent': 'Naynan12'}  # Use the specified User-Agent

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:  # Handle cases where the API returns no posts (but is still OK)
            print("None")
            sys.exit(0)

        for post in posts:
            title = post['data']['title']
            print(title)  # Print each title on a new line, no extra whitespace

    except requests.exceptions.RequestException:  # Catch network errors (ConnectionError, Timeout, etc.)
        print("None")
        sys.exit(0)

    except (ValueError, KeyError):  # Catch JSON decoding errors or missing keys in the JSON
        print("None")
        sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
        sys.exit(1)  # Indicate an error in argument passing
    else:
        top_ten(sys.argv[1])
