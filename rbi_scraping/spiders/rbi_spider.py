import scrapy
class RbiSpider(scrapy.Spider):
    DATA = 'data/rbi.txt'
    name='rbi'
    start_urls=['https://www.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009']

    def parse(self,response):
        print __file__
        with open(RbiSpider.DATA,'wb') as f:
            f.write(response.body)