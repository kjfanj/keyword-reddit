import praw
from settings import CLIENT_SECRET, CLIENT_ID, USER_AGENT
from datetime import datetime


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

    for submission in reddit.subreddit('space').hot(limit=3):
        print(submission.title)
        print("Upvotes:", submission.score)
        print("by:", submission.author)
        print("name:", submission.name)
        print("num comment:", submission.num_comments)
        print("upvote ratio:", submission.upvote_ratio)
        # print("comments**************************")
        # for comment in submission.comments:
        #     print("----------------------------------")
        #     print("user: ", comment.author)
        #     ts = int(comment.created_utc)
        #     print("at: ", datetime.utcfromtimestamp(
        #         ts).strftime('%Y-%m-%d %H:%M:%S'))
        #     print("score: ", comment.score)
        #     print(comment.body)
        print('\n')


if __name__ == "__main__":
    main()
