#!/usr/bin/python3
"""
A a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""
import requests

def number_of_subscribers(subreddit):
    """
    A method that checks if the argument passed is not a valid
    reddit subscriber
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My Reddit API Client"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200 and not response.is_redirect:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
