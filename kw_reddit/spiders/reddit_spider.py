import scrapy
import os


class RedditSpider(scrapy.Spider):
    name = "reddit"

    def start_requests(self):
        with open("spiders/subreddits.txt") as f:
            read_data = f.read()
            print(read_data)
        # files = [f for f in os.listdir('.') if os.path.isfile(f)]
        # for f in files:
        #     print(f)
        urls = [
            'https://www.reddit.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("printing response.body")
        # print(response.body)

        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
