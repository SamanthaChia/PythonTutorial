import unittest
from city_functions import city

class CityTestCase(unittest.TestCase):
    """ Tests for city_functions """

    def test_city_country(self):
        city_santiago = city('santiago','chile')
        self.assertEqual(city_santiago,"Santiago, Chile")

unittest.main()