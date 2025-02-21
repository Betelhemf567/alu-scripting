#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts of a subreddit """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'api_advanced_script:v1.0 (by /u/Naynan12)'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Debug: Print the status code
    if response.status_code != 200:
        print(None)
        return

    try:
        response_json = response.json()
        posts = response_json.get('data', {}).get('children', [])
        
        if not posts:
            print(None)
            return

        for post in posts:
            print(post['data']['title'])

    except Exception:
        print(None)

