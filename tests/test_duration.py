import unittest

from durations import Duration, Scale
from durations.constants import *
from durations.exceptions import ScaleFormatError


class TestDuration(unittest.TestCase):
    def setUp(self):
        self.test_duration = Duration('1d')

    def tearDown(self):
        pass

    def test_repr_has_valid_representation(self):
        self.assertEqual(
            self.test_duration.__repr__(),
            '<Duration 1d>'
        )

    def test_parse_simple_valid_scale(self):
        duration_representation = self.test_duration.parse('1d')
        self.assertIsInstance(duration_representation, list)

        duration_representation = duration_representation[0]
        self.assertEqual(duration_representation.value, 1.0)
        self.assertIsInstance(duration_representation.scale, Scale)
        self.assertEqual(duration_representation.scale.representation.short, 'd')

    def test_parse_composed_valid_scale(self):
        duration_representation = self.test_duration.parse('1d, 24h and 36 minutes')

        self.assertIsInstance(duration_representation, list)
        self.assertEqual(len(duration_representation), 3)

        first, second, third = duration_representation

        self.assertEqual(first.value, 1.0)
        self.assertIsInstance(first.scale, Scale)
        self.assertEqual(first.scale.representation.short, 'd')

        self.assertEqual(second.value, 24.0)
        self.assertIsInstance(second.scale, Scale)
        self.assertEqual(second.scale.representation.short, 'h')

        self.assertEqual(third.value, 36.0)
        self.assertIsInstance(third.scale, Scale)
        self.assertEqual(third.scale.representation.short, 'm')

    def test_parse_simple_malformed_scale_raises(self):
        with self.assertRaises(ScaleFormatError):
            Duration('d1')

    def test_parse_composed_malformed_scale_raises(self):
        with self.assertRaises(ScaleFormatError):
            Duration('1d h23')
