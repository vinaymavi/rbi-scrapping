#!/usr/bin/env bash
#
#Cron job file to execute processes:
#1- activate scrapy virtual environment.
#2- change directory to rbi_scrapping.
#3- run scrapping.
#4- deactivate virtual environment.
#


source  /Users/vinaymavi/envs/scrapy/bin/activate
cd  /Users/vinaymavi/appengine/rbi_scraping
scrapy crawl rbi
deactivate
exit 0
