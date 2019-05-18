class SubredditKW:
    def __init__(self, subreddit, keywords):
        self.subreddit = subreddit
        # filters out single space or when the length of keyword is less than 1
        self.keywords = list(
            filter(lambda keyword: len(keyword) >= 1 and keyword is not " ", keywords))
