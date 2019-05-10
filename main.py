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

    for submission in reddit.subreddit('space').hot(limit=3):
        print(submission.title)
        print(submission.score)
        print(submission.author)
        print("comments...?")
        for comment in submission.comments:
            print("----------------------------------")
            print(comment.author)
            print(comment.created_utc)
            print(comment.score)
            print(comment.body)
        print(submission.name)
        print(submission.num_comments)
        print(submission.upvote_ratio)
        print('\n')


if __name__ == "__main__":
    main()
