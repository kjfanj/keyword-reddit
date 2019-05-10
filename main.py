import praw
from settings import CLIENT_SECRET, CLIENT_ID, USER_AGENT


def get_subreddits(filename):
    with open(filename) as f:
        read_data = f.read()
        return read_data.split('\n')


def main():
    # parse the subreddits file
    subreddits = get_subreddits('subreddits.txt')

    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT)
    print(reddit.read_only)  # Output: True

    for submission in reddit.subreddit('learnpython').hot(limit=10):
        print(submission.title)


if __name__ == "__main__":
    main()
