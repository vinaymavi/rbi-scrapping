# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Bank(Item):
    name = Field()
    url = Field()
    file_urls = Field()


class UpdateDate(Item):
    date = Field()
