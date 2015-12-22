import scrapy
from rbi_scraping.items import UpdateDate, Bank


class RbiSpider(scrapy.Spider):
    DATA = 'data/rbi.txt'
    name = 'rbi'
    start_urls = ['https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009']

    def parse(self, response):
        updateDate = UpdateDate()
        updateDateList =response.xpath('//*[@id="example-min"]/div/table/tr/th/text()').extract()
        updateDate['date'] = updateDateList[0].split('on')[1]
        print updateDate