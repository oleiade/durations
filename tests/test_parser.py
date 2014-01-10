import unittest

from durations.parser import extract_tokens


class ParserTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_extract_tokens_simple_valid_scale(self):
        short_tokens = extract_tokens('1h')
        long_tokens = extract_tokens('1hour')
        spaced_short_tokens = extract_tokens('1 h')
        spaced_long_tokens = extract_tokens('1 hour')

        self.assertEqual(short_tokens, [('1', 'h')])
        self.assertEqual(long_tokens, [('1', 'hour')])
        self.assertEqual(spaced_short_tokens, [('1', 'h')])
        self.assertEqual(spaced_long_tokens, [('1', 'hour')])

    def test_extract_tokens_composed_valid_scale(self):
        short_tokens = extract_tokens('2d 24h')
        long_tokens = extract_tokens('2days 24hours')
        spaced_short_tokens = extract_tokens('2 d 24 h')
        spaced_long_tokens = extract_tokens('2 days 24 hours')
        mixed_short_tokens = extract_tokens('2d 24 h')
        mixed_long_tokens = extract_tokens('2days 24 hours')

        self.assertEqual(short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(long_tokens, [('2', 'days'), ('24', 'hours')])

        self.assertEqual(spaced_short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(spaced_long_tokens, [('2', 'days'), ('24', 'hours')])

        self.assertEqual(mixed_short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(mixed_long_tokens, [('2', 'days'), ('24', 'hours')])

    def test_extract_tokens_complex_scale_with_multiple_separating_chars(self):
        short_tokens = extract_tokens('2d   24h')
        long_tokens = extract_tokens('2days   24hours')
        spaced_short_tokens = extract_tokens('2   d    24 h')
        spaced_long_tokens = extract_tokens('2 days    24 hours')
        mixed_short_tokens = extract_tokens('2d    24 h')
        mixed_long_tokens = extract_tokens('2days   24 hours')

        self.assertEqual(short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(long_tokens, [('2', 'days'), ('24', 'hours')])

        self.assertEqual(spaced_short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(spaced_long_tokens, [('2', 'days'), ('24', 'hours')])

        self.assertEqual(mixed_short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(mixed_long_tokens, [('2', 'days'), ('24', 'hours')])

    def test_extract_tokens_composed_with_and_valid_scale(self):
        short_tokens = extract_tokens('2d and 24h')
        long_tokens = extract_tokens('2days and 24hours')
        spaced_short_tokens = extract_tokens('2 d and 24 h')
        spaced_long_tokens = extract_tokens('2 days and 24 hours')
        mixed_short_tokens = extract_tokens('2d and 24 h')
        mixed_long_tokens = extract_tokens('2days and 24 hours')

        self.assertEqual(short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(long_tokens, [('2', 'days'), ('24', 'hours')])

        self.assertEqual(spaced_short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(spaced_long_tokens, [('2', 'days'), ('24', 'hours')])

        self.assertEqual(mixed_short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(mixed_long_tokens, [('2', 'days'), ('24', 'hours')])

    def test_extract_tokens_simple_valid_scale_with_comma_separator(self):
        mixed_short_tokens = extract_tokens('2d, 24 h')
        mixed_long_tokens = extract_tokens('2days, 24 hours')

        self.assertEqual(mixed_short_tokens, [('2', 'd'), ('24', 'h')])
        self.assertEqual(mixed_long_tokens, [('2', 'days'), ('24', 'hours')])

