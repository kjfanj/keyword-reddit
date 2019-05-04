import scrapy
import os


class RedditSpider(scrapy.Spider):
    name = "reddit"

    def start_requests(self):
        # get all subreddits specified in the text file
        subreddits = self.parse_subreddits()

        base = "https://www.reddit.com"
        urls = []
        # append the correct subreddit url into urls
        for subreddit in subreddits:
            urls.append(base + "/r/" + subreddit)

        # now parse them using scrapy request
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("Parsing below--------------------------------------------------------------------")

        # which subreddit
        which_subreddit = response.url.split("/")[-1]
        # construct a subreddit class
        SubRedditInfo = SubRedditsInfo(which_subreddit)

        # below is each post's content based on which subreddit
        # post title-----------------------------------------------------------------------------
        titles = response.css(".scrollerItem h2::text").getall()
        print(len(titles))
        print(titles)

        # posted by------------------------------------------------------------------------------
        posted_by = response.css("._2tbHP6ZydRpjI44J3syuqC::text").getall()
        print(len(posted_by))
        print(posted_by)

        # post upvotes---------------------------------------------------------------------------
        # initially they are all duplicated, ex: ['16k', '16k', '1k', '1k']
        # need to remove even or odd number position upvotes
        upvotes = response.css(
            ".scrollerItem ._1rZYMD_4xY3gRcSS3p8ODO::text").getall()
        # removing duplicated
        new_upvotes = [upvote for index,
                       upvote in enumerate(upvotes) if index % 2 == 0]
        print(len(new_upvotes))
        print(new_upvotes)

        # comment_count--------------------------------------------------------------------------
        comment_count = response.css(".FHCV02u6Cp2zYL0fhQPsO::text").getall()
        print(len(comment_count))
        print(comment_count)

        # append post info into subreddit
        for index in range(len(titles)):
            temp_title = titles[index]
            temp_posted_by = posted_by[index]
            temp_upvotes = new_upvotes[index]
            temp_comment_count = comment_count[index]
            SubRedditInfo.addPost(
                PostInfo(temp_title, temp_upvotes, temp_posted_by, temp_comment_count))
        print("**************************************************************************************")
        SubRedditInfo.printPost()

    def parse_subreddits(self):
        # returns a list of subreddits
        # specified in subreddits.txt in the same folder
        # subreddits.txt holds all subreddits
        with open("spiders/subreddits.txt") as f:
            x = f.read()
            return x.split('\n')


# holds the subreddit name and the post
class SubRedditsInfo:
    def __init__(self, subreddit):
        self.subreddit = subreddit
        self.posts = []

    def addPost(self, post):
        self.posts.append(post)

    def printPost(self):
        for index in range(len(self.posts)):
            print("--------------------------------")
            print(self.posts[index].title)
            print(self.posts[index].upvote)
            print(self.posts[index].posted_by)
            print(self.posts[index].comment_count)
            print("--------------------------------")


# holds each posts information


class PostInfo:
    def __init__(self, title, upvote, posted_by, comment_count):
        self.title = title
        self.upvote = upvote
        self.posted_by = posted_by
        self.comment_count = comment_count
