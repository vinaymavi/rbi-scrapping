"""
This is CSV class to create csv from all xls files and send then to server.
"""

from scrapy.exceptions import NotConfigured
from scrapy import signals
from csv_processing.rbi_files import Xls, Bank, Csv as xls_csv
import logging
from csv_processing.google.gcs.gsc import GCS

logger = logging.getLogger(__name__)


class Csv(object):
    def __init__(self, item_count, xls_path, csv_path, tar_path, bank_file_path):
        self.item_count = item_count
        self.total_item_scraped = 0
        self.xls_path = xls_path
        self.csv_path = csv_path
        self.tar_path = tar_path
        self.bank_file_path = bank_file_path
        logger.info("Csv extension object created.")

    @classmethod
    def from_crawler(cls, crawler):
        logger.info("from_crawler function running.")
        if not crawler.settings.getbool('MYEXT_ENABLED'):
            raise NotConfigured
        if not crawler.settings['XLS_PATH']:
            raise NotConfigured
        if not crawler.settings['CSV_PATH']:
            raise NotConfigured
        if not crawler.settings['TAR_PATH']:
            raise NotConfigured

        item_count = crawler.settings.getint("MYEXT_ITEMCOUNT", 176)
        xls_path = crawler.settings['XLS_PATH']
        csv_path = crawler.settings['CSV_PATH']
        tar_path = crawler.settings['TAR_PATH']
        bank_file_path = crawler.settings['BANKS_NAME_FILE_NAME']
        ext = cls(item_count, xls_path, csv_path, tar_path, bank_file_path)
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
        logger.info("Start xls parsing")
        xls = Xls(self.xls_path, self.csv_path, self.tar_path)
        file_name = xls.create_csv_name()
        xls.process()
        xls_csv.validate(xls.csv_path + file_name)
        Bank.create_csv(xls_csv.get_banks(xls.csv_path + file_name), xls.csv_path + self.bank_file_path)
        GCS.copy(self.csv_path + file_name, self.csv_path + self.bank_file_path)

    def item_scraped(self, item, spider):
        self.total_item_scraped += 1
        if self.total_item_scraped % self.item_count == 0:
            logger.info("scraped %d items", self.total_item_scraped)
