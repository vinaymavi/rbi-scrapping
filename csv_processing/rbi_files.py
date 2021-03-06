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
from tempfile import NamedTemporaryFile
import shutil

logger = logging.getLogger(__name__)

# TODO test case need for this file.

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
        total = 0
        count = 0
        for f in dir_list:
            if f.endswith(".xls") or f.endswith(".xlsx"):
                file_name = self.create_csv_name(f)
                count += 1
                workbook = xlrd.open_workbook(self.xls_path + f)
                sheet = workbook.sheet_by_index(0)
                # csv file path should be exists in path.
                csv_file = open(self.csv_path + file_name, 'a')
                wr = unicodecsv.writer(csv_file, quoting=csv.QUOTE_ALL, delimiter=';')
                total += sheet.nrows
                logger.info("Total Rows=%s, %s, %s", f, count, sheet.nrows)
                first_row = True
                try:
                    for row_num in xrange(sheet.nrows):
                        if first_row:
                            first_row = False
                        else:
                            wr.writerow(sheet.row_values(row_num))
                finally:
                    csv_file.close()

        logger.info("Total banks=%s", total)

    def create_tar(self):
        """
        Create tar of processed csv files and delete them.
        :param file_name xls/xlsx file name.
        :return:
        """

    def create_csv_name(self, file_name):
        """
        convert MM_DD_YYYY format string.
        :return:
        """
        # _date_str = datetime.datetime.today().strftime("%b_%d_%Y")
        # _date_str = "branch"

        if not os.path.exists(self.csv_path):
            os.makedirs(self.csv_path)
        return file_name.split('.')[0] + ".csv"

    def rename_files(self):
        '''
        Rename xls/xlsx file with bank names.
        :return:
        '''
        dir_list = listdir(self.xls_path)
        first_line = None
        bank_name = None
        count=0
        for f in dir_list:
            if f.endswith(".xls") or f.endswith(".xlsx"):
                workbook = xlrd.open_workbook(self.xls_path + f)
                sheet = workbook.sheet_by_index(0)
                # csv file path should be exists in path.
                first_row = True
                try:
                    for row_num in xrange(sheet.nrows):
                        if first_row:
                            first_row = False
                        else:
                            first_line = sheet.row_values(row_num)
                            bank_name = first_line[0]
                            logger.info(first_line[0])
                            break
                finally:
                    workbook.release_resources()
                    os.rename(self.xls_path + f, self.xls_path + bank_name.replace(' ', '_') + "_" + f)


class Bank(object):
    @staticmethod
    def create_csv(banks, path):
        """
        Create a csv that contains all banks name.
        :param banks:list name of banks
        :param path:String path to create csv of bank names.
        :return:
        """
        csv_file = open(path, 'a')
        wr = unicodecsv.writer(csv_file, delimiter=';')
        try:
            for row in banks:
                wr.writerow([row])
        except Exception as e:
            logger.info(e.message)
        finally:
            csv_file.close()


class Csv(object):
    @staticmethod
    def validate(file_path):
        """
        Remove XLS file headers.
        :param file_path:String path of csv file.
        :return:
        """
        logger.info(file_path)
        tempfile = NamedTemporaryFile(delete=False)
        with open(file_path, 'rb') as file_csv, tempfile:
            reader = csv.reader(file_csv, delimiter=';', quotechar='"')
            writer = unicodecsv.writer(tempfile, quoting=csv.QUOTE_ALL, delimiter=';')
            for row in reader:
                row = Csv._remove_slash_n(row)
                if row[0] != "BANK":
                    writer.writerow(row)
            shutil.move(tempfile.name, file_path)

    @staticmethod
    def _remove_slash_n(row):
        #TODO line still exists for NORTH MALABAR GRAMIN BANK:197 line.
        temp = []
        for col in row:
            temp.append("""""".join("""""".join(col.splitlines()).splitlines()))
        return temp

    @staticmethod
    def get_banks(file_path):
        """
        return set of banks name.
        :param file_path: String path of csv file.
        :return: set
        """
        logger.info(file_path)
        bank_list = []
        with open(file_path, 'rb') as file_csv:
            reader = csv.reader(file_csv, delimiter=';', quotechar='"')
            for row in reader:
                bank_list.append(row[0])
        return set(bank_list)
