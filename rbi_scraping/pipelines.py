# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RbiScrapingPipeline(object):
    """
    This is temp pipeline for testing.
    """

    def process_item(self, item, spider):
        print "Pipeline calling."
        return item
