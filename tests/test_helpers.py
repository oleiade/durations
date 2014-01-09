import unittest

from durations.helpers import valid_duration


class HelpersTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_valid_duration_with_valid_simple_representation(self):
        representation = '1d'

        self.assertTrue(valid_duration(representation))

    def test_valid_duration_with_valid_complex_representation(self):
        representation = '2 days 3 hours 20 minutes'

        self.assertTrue(valid_duration(representation))

    def test_valid_duration_with_invalid_simple_representation(self):
        representation = 'd1'

        self.assertFalse(valid_duration(representation))

    def test_valid_duration_with_invalid_complex_representation(self):
        representation = 'days 2 3 hours'

        self.assertFalse(valid_duration(representation))
