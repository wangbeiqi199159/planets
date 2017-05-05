"""This file is a unit test for the get_data function
    from my_function.py
"""

import os
import unittest
import warnings
from my_function import get_data


class GetDataTestCase(unittest.TestCase):
    """Three cases unit test for get_data()
        case: (a) file is present locally
        case: (b) file is not present locally, and the URL points to a file that exists
        case: (c) URL does not point to a file that exist
    """

    def test_file_exist(self):
        """case: (a) file is present locally
            test if result of get_data() is None
        """
        url = "https://data.seattle.gov/resource/4xy5-26gy.csv"
        filename = "4xy5-26gy.csv"
        if os.path.exists(filename) is False:
            get_data(url)
        self.assertEqual(get_data(url), None)
        os.remove(filename)

    def test_file_not_exist(self):
        """case: (b) file is not present locally, and the URL points to a file that exists
            test if download succeeds and result of get_data() is True
        """
        filename = "4xy5-26gy.csv"
        url = "https://data.seattle.gov/resource/4xy5-26gy.csv"
        if os.path.exists(filename):
            os.remove(filename)
        self.assertTrue(get_data(url))

    def test_invalid_url(self):
        """case: (c) URL does not point to a file that exists
            test if get_data() will raise an exception
        """
        filename = "4xy5-26gy.csv"
        wrong_url = "https://data.seattle/resource"
        if os.path.exists(filename):
            os.remove(filename)
        with self.assertRaises(ValueError) as context:
            get_data(wrong_url)
        self.assertTrue('URL is not valid' in str(context.exception))

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    unittest.main()
