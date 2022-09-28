#!/usr/bin/env python3 
import unittest
import myprogram
import card_validator

class TestValidator(unittest.TestCase):

    def test_valid_luhncheck(self):
        bval = card_validator.is_luhn_valid(4111111111111111)
        self.assertEqual(bval, True)
        print("\nTestCase:   Valid Luhn10 Check - Passed")

    def test_invalid_luhncheck(self):
        bval = card_validator.is_luhn_valid(1234567890123456)
        self.assertEqual(bval, False)
        print("\nTestCase: Invalid Luhn10 Check - Passed")

class TestProgram(unittest.TestCase):

    def test_valid_data(self):
        myprogram.data_processor("Add Tom 4111111111111111 $1000")
        self.assertEqual(myprogram.data_dict['Tom'], {'bal': 1000, 'card': '4111111111111111', 'status': 'valid'})
        print("\nTestCase:   Valid AddData - Passed")

    def test_invalid_data(self):
        myprogram.data_processor("Add Quincy 1234567890123456 $2000")
        self.assertEqual(myprogram.data_dict['Quincy'],{'bal': 'error', 'card': '1234567890123456', 'status': 'invalid'})
        print("\nTestCase: Invalid AddData - Passed")

    # def test_stdin(self):
    #     myprogram

    # def test_fileinput(self):
    #     pass


if __name__ == '__main__':
    unittest.main()