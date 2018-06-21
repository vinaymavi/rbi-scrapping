import scrapy
from rbi_scraping.items import UpdateDate, Bank
import logging

logger = logging.getLogger(__name__)

class RbiSpider(scrapy.Spider):
    DATA = 'data/rbi.txt'
    # TODO configure banks.csv in global settings.py

    name = 'rbi'   
    start_urls = ['https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009']
    file_urls = []
    bank_names = []

    def parse(self, response):
        update_date = UpdateDate()
        update_date_list = response.xpath('//*[@id="example-min"]/div/table/tr/th/text()').extract()
        update_date['date'] = update_date_list[0].split('on')[1]
        banks_url_list = response.xpath('//*[@id="example-min"]/div/table/tr[3]/td/table/tr/td/a/@href').extract()
        logger.info('*****************URLs Info******************')
        logger.info('Bank list length = '+str(len(banks_url_list)))
        for index, val in enumerate(banks_url_list):
            bank = Bank()
            logger.info(index)
            logger.info(val)
            bank['url'] = val
            https_val = val.replace('http', 'https')
            bank['file_urls'] = [https_val]
            self.file_urls.append(bank)
        logger.info('********************************************')
        return self.file_urls
