import scrapy
import os


class RedditSpider(scrapy.Spider):
    name = "reddit"

    def start_requests(self):
        print(self.parse_subreddits())
        urls = [
            'https://www.reddit.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("Parsing below--------------------------------------------------------------------")
        print(response.css('title'))
        # print(response.body)

        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
    def parse_subreddits(self):
        print("parsing subreddits---------------------------------------------------------------")
        with open("spiders/subreddits.txt") as f:
            x = f.read()
            return x.split('\n')
