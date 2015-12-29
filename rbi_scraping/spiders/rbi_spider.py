import scrapy
from rbi_scraping.items import UpdateDate, Bank
from csv_processing.xls import Bank as bank_csv


class RbiSpider(scrapy.Spider):
    DATA = 'data/rbi.txt'
    # TODO configure banks.csv in global settings.py
    BANKS_NAME_FILE_NAME = 'banks.csv'
    name = 'rbi'
    start_urls = ['https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009']
    file_urls = []
    bank_names = []

    def parse(self, response):
        update_date = UpdateDate()
        update_date_list = response.xpath('//*[@id="example-min"]/div/table/tr/th/text()').extract()
        update_date['date'] = update_date_list[0].split('on')[1]
        banks_url_list = response.xpath('//*[@id="example-min"]/div/table/tr[2]/td/table/tr/td/a/@href').extract()
        banks_name_list = response.xpath('//*[@id="example-min"]/div/table/tr[2]/td/table/tr/td/a/text()').extract()
        for index, val in enumerate(banks_url_list):
            bank = Bank()
            bank['url'] = val
            https_val = val.replace('http', 'https')
            bank['file_urls'] = [https_val]
            self.file_urls.append(bank)
        csv_path = self.crawler.settings['CSV_PATH']
        bank_csv.create_csv(banks_name_list, csv_path + RbiSpider.BANKS_NAME_FILE_NAME)
        return self.file_urls
