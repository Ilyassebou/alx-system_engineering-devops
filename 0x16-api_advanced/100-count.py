#!/usr/bin/python3
""" Function to count words in all hot posts of a given Reddit subreddit. """
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
     Recursive function that queries the Reddit API, parses the title of all
     hot articles, and prints a sorted count of given keywords
    """
    if after is None:
        base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        base_url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after
        )

    headers = {'User-Agent': 'Agent Uche'}
    params = {'after': after} if after else {}

    response = requests.get(
        base_url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        title = post['data']['title'].lower()
        for keyword in word_list:
            keyword = keyword.lower()
            if (
                keyword in title
                and not title.startswith(keyword + '.')
                and not title.startswith(keyword + '!')
                and not title.startswith(keyword + '_')
            ):
                counts[keyword] = counts.get(keyword, 0) + 1

    next_page = data.get('data', {}).get('after')
    if next_page:
        count_words(subreddit, word_list, after=next_page, counts=counts)
    else:
        sorted_counts = sorted(
            counts.items(), key=lambda item: (-item[1], item[0])
        )
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
