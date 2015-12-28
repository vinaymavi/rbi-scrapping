import unittest
from csv_processing.xls import Xls


class CsvTest(unittest.TestCase):
    def test_process(self):
        XLS_PATH = '/Users/vinaymavi/rbi_ifsc_xls/full/'
        CSV_PATH = '/Users/vinaymavi/rbi_ifsc_xls/csv/'
        TAR_PATH = '/Users/vinaymavi/rbi_ifsc_xls/old/'
        xls = Xls(XLS_PATH, CSV_PATH, TAR_PATH)
        xls.process()


if __name__ == '__main__':
    unittest.main()
