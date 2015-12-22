import scrapy
from rbi_scraping.items import UpdateDate, Bank


class RbiSpider(scrapy.Spider):
    DATA = 'data/rbi.txt'
    name = 'rbi'
    start_urls = ['https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009']
    file_urls = []

    def parse(self, response):
        update_date = UpdateDate()
        update_dateList = response.xpath('//*[@id="example-min"]/div/table/tr/th/text()').extract()
        update_date['date'] = update_dateList[0].split('on')[1]
        bank_url_list = response.xpath('//*[@id="example-min"]/div/table/tr[2]/td/table/tr/td/a/@href').extract()
        for index, val in enumerate(bank_url_list):
            bank = Bank()
            bank['url'] = val
            https_val = val.replace('http', 'https')
            bank['file_urls'] = [https_val]
            self.file_urls.append(bank)
        return self.file_urls
