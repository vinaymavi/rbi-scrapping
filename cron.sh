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
d=$(date +%y-%m-%d)
mkdir "/Users/vinaymavi/rbi_ifsc_xls/csv/old_csv/$d"
mv -f /Users/vinaymavi/rbi_ifsc_xls/csv/*.csv "/Users/vinaymavi/rbi_ifsc_xls/csv/old_csv/$d"
cd /Users/vinaymavi/rbi_ifsc_xls
tar -cvzf "$d.tar.gz" full
mv *.tar.gz tar/
rm -rvf full
exit 0
