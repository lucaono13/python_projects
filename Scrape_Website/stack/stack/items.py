# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class StackItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    age = Field()
    yrs_rem = Field()
    fa_type = Field()
    cont_19 = Field()
    position = Field()
    team = Field()
    pass
