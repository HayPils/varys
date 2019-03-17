# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2;

class PostgresPipeline(object):
    def __init__(self, db_settings):
        self.db_settings = db_settings
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_settings = crawler.settings.get('DATABASE')
        )

    def open_spider(self, spider):
        hostname = self.db_settings['DB_HOST']
        username = self.db_settings['DB_USER']
        password = self.db_settings['DB_PASS'] 
        database = self.db_settings['DB_NAME']
        port = self.db_settings['DB_PORT']
        #self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
        #self.cur = self.connection.cursor()

    def close_spider(self, spider):
        #self.cur.close()
        #self.connection.close()
        pass

    def process_item(self, item, spider):
        #self.cur.execute("insert into quotes_content(content,author) values(%s,%s)",(item['content'],item['author']))
        #self.connection.commit()
        return item 
        