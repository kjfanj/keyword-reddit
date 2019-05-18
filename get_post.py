import praw
from prawcore import NotFound
# keys for praw
from settings import CLIENT_SECRET, CLIENT_ID, USER_AGENT, MONGO_URI, APP_PW, MY_GMAIL
from datetime import datetime, timezone
# class def
from SubredditKW import SubredditKW
import smtplib
from email.mime.text import MIMEText
from Posts import Posts


def subreddit_exists(subreddit, reddit):
    """
    return true if subreddit exist, else false
    """
    exists = True
    try:
        reddit.subreddits.search_by_name(subreddit, exact=True)
    except NotFound:
        exists = False

    return exists


def get_lines(filename):
    """
    return a list of each line in the file
    """
    with open(filename) as f:
        read_data = f.read()
        return read_data.split('\n')


def get_subreddit_kws(lines):
    """
    param
    return a list of SubredditKW after parsing
    """
    subreddit_kw = []
    for line in lines:
        split_line = line.split(',')
        # make sure to not add empty line
        if len(split_line) > 1:
            # position 0 holds subreddit
            cur_subreddit = split_line[0]
            # position >=1 holds all the keywords
            cur_keywords = split_line[1:]
            subreddit_kw.append(SubredditKW(cur_subreddit, cur_keywords))
    return subreddit_kw


def send_email(kw, subreddit, reddit_permalink, url, title, total, body, created_time, by_user, is_self):
    """
    take in the keyword found from {some subreddit}, and send the url and title to yourself
    """
    # message formatting
    formatted_time = datetime.utcfromtimestamp(
        created_time).strftime('%Y-%m-%d %H:%M:%S')
    body_to_display = body if body else "No self posts"
    url_to_display = "" if is_self else url
    permalink_to_display = "https://www.reddit.com{}".format(reddit_permalink)
    SUBJECT = "Keyword: \"{}\" found from Subreddit: {}".format(
        kw, subreddit)
    msg = "Title: \"{}\"\n{}\n\nBody:\n{}\n\nCreated: {}\nBy: u/{}\nReddit post link: {}\n\n\nTotal sent: {}".format(
        title, url_to_display, body_to_display, formatted_time, by_user, permalink_to_display, total)
    FROM = MY_GMAIL
    TO = MY_GMAIL
    msg = MIMEText(msg)
    msg['Subject'] = SUBJECT
    msg['To'] = TO
    msg['From'] = FROM
    # login and send email
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(MY_GMAIL, APP_PW)
    # send from my gmail to my gmail
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()


def look_up_loop():
    """
    looping for new searches
    first parse,
    then connect praw,
    then start new search on all listed subreddit,
    then check if kw exist in title, if found send email
    """
    # sent_posts used for Post's class variable to avoid sending sent posts
    sent_posts = Posts()

    # parsing
    lines = get_lines('subreddits.txt')
    subreddit_kws = get_subreddit_kws(lines)
    # connecting praw
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT)
    print("----------------------------------------------------")
    print(" # New searches coming through. {}\n".format(
        datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))

    # loop through all the SubredditKW object
    for subreddit_kw in subreddit_kws:
        # check if subreddit specified in the file exists
        if subreddit_exists(subreddit_kw.subreddit, reddit):
            # printing out the subreddit and keyword we are looking for
            print(" * r/{} -- {}".format(subreddit_kw.subreddit, subreddit_kw.keywords))
            # loop through the submission of the subreddit based on the new(limit=10) method
            for submission in reddit.subreddit(subreddit_kw.subreddit).new(limit=10):
                # loop through the keywords in SubredditKW object then find matching
                for kw in subreddit_kw.keywords:
                    # if kw found and doesnt exist in sent_posts then send the email to myself
                    if not sent_posts.check_if_id_exists(submission.id) and kw.lower() in submission.title.lower():
                        print(" ********** \"{}\" found from {}, sending email".format(
                            kw, subreddit_kw.subreddit))
                        # kw found! sending email
                        send_email(kw, subreddit_kw.subreddit, submission.permalink,
                                   submission.url, submission.title,
                                   len(sent_posts.ids) +
                                   1, submission.selftext,
                                   submission.created_utc, submission.author, submission.is_self)
                        # and add it to sent_posts so no emailing for repetitive submission
                        sent_posts.add_post(submission.id)
        # subreddit does not exist, inform the user to check subreddits.txt again
        else:
            print(" - r/{} does not exist, please check subreddits.txt again".format(
                subreddit_kw.subreddit))
