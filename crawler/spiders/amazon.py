# -*- coding: utf-8 -*-
import scrapy

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    burl = 'https://www.amazon.com/'

    def start_requests(self):
        search = 'snow+boots'
        start_url = f'{self.burl}s?k={search}'
        yield scrapy.Request(start_url, self.parse_prod)

    def parse_prod(self, response):
        # normal listings
        listing_urls = response.css('div.sg-row > div > div > span > div.s-result-list.sg-row > div > div > div > div > div > div > div > div > span > a::attr(href)').getall()
        # sponsored listings
        listing_urls += response.css('div.sg-row > div > div > span > div.s-result-list.sg-row > div > div > div > div > div > div > div > div > div > div > span > a')
        print(len(listing_urls));
        pass