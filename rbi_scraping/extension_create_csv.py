"""
This is CSV class to create csv from all xls files and send then to server.
"""

from scrapy.exceptions import NotConfigured
from scrapy import signals

import logging
logger = logging.getLogger(__name__)


class Csv(object):
    def __init__(self, item_count):
        self.item_count = item_count
        self.total_item_scraped = 0
        logger.info("Csv extension object created.")

    @classmethod
    def from_crawler(cls, crawler):
        logger.info("from_crawler function running.")
        if not crawler.settings.getbool('MYEXT_ENABLED'):
            raise NotConfigured

        item_count = crawler.settings.getint("MYEXT_ITEMCOUNT", 176)
        ext = cls(item_count)
        # connect the extension object to signals
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        return ext

    # connect extension object signals
    def spider_opened(self, spider):
        logger.info("opened spider %s", spider.name)

    def spider_closed(self, spider):
        logger.info("closed spider %s", spider.name)

    def item_scraped(self, item, spider):
        self.total_item_scraped += 1
        if self.total_item_scraped % self.item_count == 0:
            logger.info("scraped %d items", self.total_item_scraped)
