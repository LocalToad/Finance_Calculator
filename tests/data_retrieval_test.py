import unittest
import datetime
from unittest.mock import patch

from freezegun import freeze_time

import Data_Retrieval
import Income


class TestDataRetrieval(unittest.TestCase):
    default_dict = {}

    saved_date = "2012-01-01"
    saved_list = [1, 2, 3]
    saved_dict = {saved_date: saved_list}

    @freeze_time("2012-12-01")
    @patch('Data_Retrieval.writeJSONtoPath')
    @patch('Data_Retrieval.grabJSONifExists', return_value=default_dict)
    def test_income_report_success_no_saved_list(self, mock_grab_json, mock_write_json):
        sample_date = datetime.date(2012, 12, 1)

        date_string = str(sample_date)

        path = "Income_Report.json"
        sample_list = [0, 1, 2]
        expected = {f"{date_string}": sample_list}
        result = Data_Retrieval.generateReport(path, sample_list)
        assert result == expected

    @freeze_time("2012-12-01")
    @patch('Data_Retrieval.writeJSONtoPath')
    @patch('Data_Retrieval.grabJSONifExists', return_value=saved_dict)
    def test_income_report_success_saved_list(self, mock_grab_json, mock_write_json):
        sample_date = datetime.date(2012, 12, 1)
        date_string = str(sample_date)

        path = "Income_Report.json"
        sample_list = [4, 5, 6]
        expected = {self.saved_date: self.saved_list, date_string: sample_list}
        result = Data_Retrieval.generateReport(path, sample_list)
        assert result == expected