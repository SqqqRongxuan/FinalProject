import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    def parse(self, response):
        pass
