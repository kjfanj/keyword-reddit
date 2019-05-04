import scrapy
import os


class RedditSpider(scrapy.Spider):
    name = "reddit"

    def start_requests(self):
        subreddits = self.parse_subreddits()
        base = "https://www.reddit.com"
        urls = []
        for subreddit in subreddits:
          urls.append(base + "/r/" + subreddit)
          
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("Parsing below--------------------------------------------------------------------")

        # item title
        titles = response.css(".scrollerItem h2::text").getall()
        print(titles)
        # upvotes
        upvotes = response.css(".scrollerItem ._1rZYMD_4xY3gRcSS3p8ODO::text").getall()
        print(upvotes)
        # content

        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
    
    def parse_subreddits(self):
        # returns a list of subreddits 
        # specified in subreddits.txt in the same folder
        # subreddits.txt holds all 
        print("parsing subreddits---------------------------------------------------------------")
        with open("spiders/subreddits.txt") as f:
            x = f.read()
            return x.split('\n')
