"""
Convert and concatnation of downloaded .xls files.
"""
import xlrd
import csv
import unicodecsv
from os import listdir
import os
import datetime
import logging

logger = logging.getLogger(__name__)


class Xls(object):
    xls_path = ''
    csv_path = ''
    tar_path = ''

    def __init__(self, xls_path, csv_path, tar_path):
        """

        :param xls_path:String downloaded xls file path.
        :param csv_path:String path to save created csv.
        :param tar_path:String path tar processed xls.
        :return:
        """
        self.xls_path = xls_path
        self.csv_path = csv_path
        self.tar_path = tar_path

    def process(self):
        """
        Process all xls files and convert it to csv.
        :return:
        """
        dir_list = listdir(self.xls_path)
        file_name = self._create_csv_name()+".csv"
        total = 0
        count = 0
        for f in dir_list:
            logger.info(f)
            print f
            if f.endswith(".xls"):
                count += 1
                workbook = xlrd.open_workbook(self.xls_path + f)
                sheet = workbook.sheet_by_index(0)
                # csv file path should be exists in path.
                csv_file = open(self.csv_path + file_name, 'a')
                wr = unicodecsv.writer(csv_file, quoting=csv.QUOTE_ALL, delimiter=';')
                total += sheet.nrows
                logger.info("Total Rows=%s, %s, %s", f, count, sheet.nrows)
                try:
                    for row_num in xrange(sheet.nrows):
                        wr.writerow(sheet.row_values(row_num))
                finally:
                    csv_file.close()

        logger.info("Total banks=%s", total)

    def create_tar(self):
        """
        Create tar of processed csv files and delete them.
        :return:
        """

    def _create_csv_name(self):
        """
        convert MM_DD_YYYY format string.
        :return:
        """
        _date_str = datetime.datetime.today().strftime("%b_%d_%Y")

        if not os.path.exists(self.csv_path):
            os.makedirs(self.csv_path)
        return _date_str
