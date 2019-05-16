import praw
# keys for praw
from settings import CLIENT_SECRET, CLIENT_ID, USER_AGENT, MONGO_URI, APP_PW, MY_GMAIL
from datetime import datetime
# class def
from SubredditKW import SubredditKW
import smtplib
from email.mime.text import MIMEText


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


def send_email(kw, subreddit, url, title):
    """
    take in the keyword found from {some subreddit}, and send the url and title to yourself
    """
    # message formatting
    SUBJECT = "Keyword: \"{}\" found from Subreddit: {}".format(kw, subreddit)
    msg = "Title: \"{}\"\n {}".format(title, url)
    TO = MY_GMAIL
    FROM = MY_GMAIL

    msg = MIMEText(msg)
    msg['Subject'] = SUBJECT
    msg['To'] = TO
    msg['From'] = FROM

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(MY_GMAIL, APP_PW)
    # send from my gmail to my gmail
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()


def look_up_loop():
    """
    main looping for new searches
    first parse,
    then connect praw,
    then start new search on all subreddit,
    then check if kw exist in title, if found send email
    """
    # parsing
    lines = get_lines('subreddits.txt')
    subreddit_kws = get_subreddit_kws(lines)
    # connecting praw
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT)
    # loop through all the SubredditKW object
    for subreddit_kw in subreddit_kws:
        # loop through the submission of the subreddit based on the new method
        for submission in reddit.subreddit(subreddit_kw.subreddit).hot(limit=10):
            # loop through the keywords in SubredditKW object then find matching
            for kw in subreddit_kw.keywords:
                # if found then send the email to myself
                if kw in submission.title:
                    # kw found! sending email
                    send_email(kw, subreddit_kw.subreddit,
                               submission.url, submission.title)
