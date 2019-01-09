import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Tests for 'name_function.py' """

    def test_first_last_name(self):
        formatted_name = get_formatted_name('sam', 'chia')
        self.assertEqual(formatted_name, 'Sam Chia')
    
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name(
            'sam', 'chia', 'eileen')
        self.assertEqual(formatted_name, 'Sam Eileen Chia')
unittest.main()