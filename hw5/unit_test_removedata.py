"""This file is an unit test for remove_data()function from my_function.py
"""
import os
import unittest
from my_function import remove_data


class RemoveDataTestCase(unittest.TestCase):
    """Unit test for remove_data() function
        test case: if file is present locally
    """

    def test(self):
        """This function test returns of remove_data() under test case.
            1.If file is present locally, test if return of remove_data() is True.
             2. If file is not present locally, if return of remove)data() raise an exception
        """
        filename = "4xy5-26gy.csv"
        if os.path.exists(filename):
            self.assertTrue(remove_data(filename))
        else:
            with self.assertRaises(ValueError) as context:
                remove_data(filename)
            self.assertTrue(
                'File does not exist.' in str(context.exception)
                )

if __name__ == '__main__':
    unittest.main()
