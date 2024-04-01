import unittest
from city_functions import place


class TestCity(unittest.TestCase):

    def test_city_country(self):
        message = place('new', 'chile')
        self.assertEquals(message, 'New, Chile')


unittest.main()
