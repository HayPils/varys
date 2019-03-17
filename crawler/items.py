# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ListingItem(scrapy.Item):
    prod_id = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    bsr = scrapy.Field()

class ReviewItem(scrapy.Item):
    list_id = scrapy.Field()
    headline = scrapy.Field()
    body = scrapy.Field()
    rating = scrapy.Field()
    votes = scrapy.Field()
    date_pub = scrapy.Field()

class FaqItem(scrapy.Item):
    list_id = scrapy.Field()
    question = scrapy.Field()
    answer = scrapy.Field()
    votes = scrapy.Field()
    date_ans = scrapy.Field()