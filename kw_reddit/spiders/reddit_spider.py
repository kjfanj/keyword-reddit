import scrapy


class RedditSpider(scrapy.Spider):
    name = "reddit"

    def start_requests(self):
        urls = [
            'https://www.reddit.com/r/pathofexile/',
            # 'http://quotes.toscrape.com/page/1/',
            # 'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("printing response.body")
        print(response.body)
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
