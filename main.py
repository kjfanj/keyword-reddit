import praw
# keys for praw
from settings import CLIENT_SECRET, CLIENT_ID, USER_AGENT
from datetime import datetime
# class def
from SubredditKW import SubredditKW


def get_lines(filename):
    """
    return a list of each line in the file
    """
    with open(filename) as f:
        read_data = f.read()
        return read_data.split('\n')


def get_subreddit_kws(lines):
    """
    return a list of SubredditKW after parsing 
    """
    subreddit_kw = []
    for line in lines:
        split_line = line.split(',')
        # position 0 holds subreddit
        cur_subreddit = split_line[0]
        # position >=1 holds all the keywords
        cur_keywords = split_line[1:]
        subreddit_kw.append(SubredditKW(cur_subreddit, cur_keywords))
    return subreddit_kw


def main():
    lines = get_lines('subreddits.txt')
    subreddit_kws = get_subreddit_kws(lines)

    for subreddit_kw in subreddit_kws:
        print(subreddit_kw.subreddit)
        print(subreddit_kw.keywords)

    # reddit = praw.Reddit(client_id=CLIENT_ID,
    #                      client_secret=CLIENT_SECRET,
    #                      user_agent=USER_AGENT)

    # for submission in reddit.subreddit('space').hot(limit=3):
    #     print("Title:", submission.title)
    #     print("self text:")
    #     print("-------------------------------------------------------------")
    #     print(submission.selftext)
    #     print("-------------------------------------------------------------")
    #     print("Upvotes:", submission.score)
    #     print("By:", submission.author)
    #     print("Num comment:", submission.num_comments)
    #     print("Upvote ratio:", submission.upvote_ratio)
    #     print("")

    # comment example here
    # print("comments**************************")
    # for comment in submission.comments:
    #     print("----------------------------------")
    #     print("user:", comment.author)
    #     ts = int(comment.created_utc)
    #     print("at:", datetime.utcfromtimestamp(
    #         ts).strftime('%Y-%m-%d %H:%M:%S'))
    #     print("score:", comment.score)
    #     print(comment.body)


# if __name__ == "__main__":
#     main()
