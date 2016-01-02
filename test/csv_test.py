import unittest
from csv_processing.rbi_files import Xls, Bank, Csv


class CsvTest(unittest.TestCase):
    def test_process(self):
        XLS_PATH = '/Users/vinaymavi/rbi_ifsc_xls/'
        CSV_PATH = '/Users/vinaymavi/rbi_ifsc_xls/csv/'
        TAR_PATH = '/Users/vinaymavi/rbi_ifsc_xls/old/'
        xls = Xls(XLS_PATH, CSV_PATH, TAR_PATH)
        xls.process()

    def test_banks_list_cration(self):
        CSV_PATH = '/Users/vinaymavi/rbi_ifsc_xls/csv/'
        BRANCH_CSV_PATH = "/Users/vinaymavi/rbi_ifsc_xls/csv/old_csv/Dec_31_2015.csv"
        Bank.create_csv(Csv.get_banks(BRANCH_CSV_PATH), CSV_PATH + 'banks.csv')

    def test_csv_validation(self):
        CSV_PATH = "/Users/vinaymavi/rbi_ifsc_xls/csv/old_csv/Jan_02_2016.csv"
        Csv.validate(CSV_PATH)


if __name__ == '__main__':
    unittest.main()
