import praw
# keys for praw
from settings import CLIENT_SECRET, CLIENT_ID, USER_AGENT, MONGO_URI
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


def look_up_loop():
    lines = get_lines('subreddits.txt')
    subreddit_kws = get_subreddit_kws(lines)

    # for subreddit_kw in subreddit_kws:
    #     print(subreddit_kw.subreddit)
    #     print(subreddit_kw.keywords)

    print("new search")
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT)
    # lol = []
    for submission in reddit.subreddit('testabot').new(limit=10):
        if("hello there" in submission.title):
            print("post found")
        # kw_col.insert_one(submission)
        # lol.append(submission)
        # print("Title:", submission.title)
        # print("self text:")
        # print("-------------------------------------------------------------")
        # print(submission.selftext)
        # print("-------------------------------------------------------------")
        # print("Upvotes:", submission.score)
        # print("By:", submission.author)
        # print("Num comment:", submission.num_comments)
        # print("Upvote ratio:", submission.upvote_ratio)
        # print("")

    # x = kw_col.find_one(lol[0])

    # Print the result to the screen
    # print(x)

    # Close the connection
    # client.close()
    # for lolol in lol:
    #     print(lolol.is_self)
    # print(len(lol))
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


look_up_loop()
