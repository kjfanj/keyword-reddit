class SubredditKW:
    def __init__(self, subreddit, keywords):
        self.subreddit = subreddit
        self.keywords = list(
            filter(lambda keyword: len(keyword) >= 1 and keyword is not " ", keywords))
