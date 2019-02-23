# -*- coding: utf-8 -*-
import scrapy


class AmazonReviewsSpider(scrapy.Spider):
    name = 'amazon_reviews'
    allowed_domains = ['amazon.com']
    start_urls = []

    def __init__(self, category="", **kwargs):
        super().__init__(**kwargs)  # python3
        for i in range(1, 2): 
            self.start_urls.append(base_url + str(i))

    def parse(self, response):
        data = response.css('#cm_cr-review_list') 
        
        star_rating = data.css('.review-rating')

        comments = data.css('.review-text')
        count = 0

        for review in star_rating:
            yield{
                    'stars': ''.join(review.xpath('.//text()').extract()),
                    'comment': ''.join(comments[count].xpath(".//text()").extract())
                    }
            count=count+1
