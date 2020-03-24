import scrapy


class QuotesSpider(scrapy.Spider):
    name = "Quotes"

    def start_requests(self):
        urls = [
            'https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        print(filename)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)