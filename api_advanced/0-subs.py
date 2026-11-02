"""Retrieve data from Reddit"""
import requests
def number_of_subscribers(subreddit):
    subs = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json", headers = {"User-Agent": "windows:(ALU Student Project) (by /u/ggp_user)"}
        )
    print(subs)
    print(subs.json())

if __name__ ==  "__main__":
    subreddit = "python"
    number_of_subscribers(subreddit)