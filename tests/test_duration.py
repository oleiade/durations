import unittest

from durations import Duration, Scale
from durations.constants import *
from durations.exceptions import ScaleFormatError


class TestDuration(unittest.TestCase):
    def setUp(self):
        self.test_duration = Duration('1d')

    def tearDown(self):
        pass

    def test_extract_tokens_simple_valid_scale(self):
        short_tokens = self.test_duration.extract_tokens('1h')
        long_tokens = self.test_duration.extract_tokens('1hour')
        spaced_short_tokens = self.test_duration.extract_tokens('1 h')
        spaced_long_tokens = self.test_duration.extract_tokens('1 hour')

        self.assertEqual(short_tokens, [('1', 'h')])
        self.assertEqual(long_tokens, [('1', 'hour')])
        self.assertEqual(spaced_short_tokens, [('1', 'h')])
        self.assertEqual(spaced_long_tokens, [('1', 'hour')])

    def test_extract_tokens_composed_valid_scale(self):
        short_tokens = self.test_duration.extract_tokens('2d 24h')
        long_tokens = self.test_duration.extract_tokens('2days 24hours')
        spaced_short_tokens = self.test_duration.extract_tokens('2 d 24 h')
        spaced_long_tokens = self.test_duration.extract_tokens('2 days 24 hours')
        mixed_short_tokens = self.test_duration.extract_tokens('2d 24 h')
        mixed_long_tokens = self.test_duration.extract_tokens('2days 24 hours')

        self.assertEqual(short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(long_tokens, [('2', 'days'), ('24', 'hours')])

        self.assertEqual(spaced_short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(spaced_long_tokens, [('2', 'days'), ('24', 'hours')])

        self.assertEqual(mixed_short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(mixed_long_tokens, [('2', 'days'), ('24', 'hours')])

    def test_extract_tokens_complex_scale_with_multiple_separating_chars(self):
        short_tokens = self.test_duration.extract_tokens('2d   24h')
        long_tokens = self.test_duration.extract_tokens('2days   24hours')
        spaced_short_tokens = self.test_duration.extract_tokens('2   d    24 h')
        spaced_long_tokens = self.test_duration.extract_tokens('2 days    24 hours')
        mixed_short_tokens = self.test_duration.extract_tokens('2d    24 h')
        mixed_long_tokens = self.test_duration.extract_tokens('2days   24 hours')

        self.assertEqual(short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(long_tokens, [('2', 'days'), ('24', 'hours')])

        self.assertEqual(spaced_short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(spaced_long_tokens, [('2', 'days'), ('24', 'hours')])

        self.assertEqual(mixed_short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(mixed_long_tokens, [('2', 'days'), ('24', 'hours')])

    # def test_extract_tokens_simple_valid_scale_with_comma_separator(self):
    #     mixed_short_tokens = self.test_duration.extract_tokens('2d, 24 h')
    #     mixed_long_tokens = self.test_duration.extract_tokens('2days, 24 hours')

    #     self.assertEqual(mixed_short_tokens, [('2', 'd'), ('24', 'h')])
    #     self.assertEqual(mixed_long_tokens, [('2', 'days'), ('24', 'hours')])

    def test_parse_simple_valid_scale(self):
        duration_representation = self.test_duration.parse('1d')
        self.assertIsInstance(duration_representation, list)

        duration_representation = duration_representation[0]
        self.assertEqual(duration_representation.value, 1.0)
        self.assertIsInstance(duration_representation.scale, Scale)
        self.assertEqual(duration_representation.scale.representation.short, 'd')

    def test_parse_composed_valid_scale(self):
        duration_representation = self.test_duration.parse('1d 24h')

        self.assertIsInstance(duration_representation, list)
        self.assertEqual(len(duration_representation), 2)

        first, second = duration_representation

        self.assertEqual(first.value, 1.0)
        self.assertIsInstance(first.scale, Scale)
        self.assertEqual(first.scale.representation.short, 'd')

        self.assertEqual(second.value, 24.0)
        self.assertIsInstance(second.scale, Scale)
        self.assertEqual(second.scale.representation.short, 'h')

    def test_parse_simple_malformed_scale_raises(self):
        with self.assertRaises(ScaleFormatError):
            Duration('d1')

    def test_parse_composed_malformed_scale_raises(self):
        with self.assertRaises(ScaleFormatError):
            Duration('1d h23')
