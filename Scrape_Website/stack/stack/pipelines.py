# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
#from scrapy.conf import settings
from scrapy.exceptions import DropItem
#from scrapy import log

class MongoDBPipeline(object):
    """
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DF']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing{0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Player added to MongoDB database!", level = log.DEBUG, spider=spider)
        return item
    """

    collection_name = "scrapy_items"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(mongo_uri = crawler.settings.get('MONGODB_PORT'),mongo_db = crawler.settings.get('MONGODB_DF','items'))

    #def open_spider(self,spider):
        #self.client.close()

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            scrapy.log.msg("Player added to MongoDB database!", level = log.DEBUG, spider= spider)
        return item
