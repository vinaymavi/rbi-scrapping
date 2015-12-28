"""
Cron job file to execute processes:
1- activate scrapy virtual environment.
2- change directory to rbi_scrapping.
3- run scrapping.
4- deactivate virtual environment.
"""

SCRAPY_ENV = "/Users/vinaymavi/envs/scrapy/bin/activate"
PROJECT_PATH = "/Users/vinaymavi/appengine/rbi_scraping"
call(['source', SCRAPY_ENV])
call(['cd', PROJECT_PATH])
call(["scrapy", "crawl", "rbi"])
call(['deactivate'])
