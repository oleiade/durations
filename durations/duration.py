from collections import namedtuple
from itertools import izip
from functools import partial
from types import MethodType

from durations.exceptions import ScaleFormatError
from durations.scales import Scale
from durations.constants import *


DurationRepresentation = namedtuple(
    'DurationRepresentation',
    ['value', 'scale']
)


class Duration(object):
    """Duration representation class

    Duration objects parses an input duration representation
    string, and provides a set of methods to retrieve and
    convert it's value to other units.

    Example:
        >>> d = Duration('1m')
        >>> d.to_seconds()
        60.0
        >>> d.to_hours()
        0.02
        >>> d = Duration('3 hours')
        >>> d.to_minutes()
        180.0
    """
    def __init__(self, representation, *args, **kwargs):
        self.parsed_durations = self.parse(representation)
        self.seconds = self._compute_seconds_value()

    def __str__(self):
        return '<Duration {}>'.format(self.representation)

    def __repr__(self):
        return self.__str__()

    def _compute_seconds_value(self):
        seconds = 0

        for duration in self.parsed_durations:
            seconds += duration.value * duration.scale.conversion_unit

        return seconds

    def compute_char_token(self, c):
        if c.isdigit():
            return SCALE_TOKEN_DIGIT
        elif c.isalpha():
            return SCALE_TOKEN_ALPHA

        return None

    def extract_tokens(self, representation, sep=" "):
        buff = ""
        elements = []
        last_index = 0
        last_token = None

        for index, c in enumerate(representation):
            if c == sep:
                elements.append(buff)
                buff = ""
                last_token = None
            else:
                token = self.compute_char_token(c)
                if (token is not None and last_token is not None and token != last_token):
                    elements.append(buff)
                    buff = c
                else:
                    buff += c
                last_token = token

        # push the content left in representation
        # in the elements list
        elements.append(buff)

        return zip(elements[::2], elements[1::2])

    def parse(self, representation):
        """Parses a duration string representation


        :param  representation: duration as a string, example: '1d' (day),
                                '34minutes' (minutes), '485s' (seconds)...
        :type   representation: string

        :returns: the parsed duration representation
        :rtype: DurationRepresentation
        """
        elements = self.extract_tokens(representation)

        try:
            scales = [DurationRepresentation(float(p[0]), Scale(p[1])) for p in elements]
        except ValueError:
            raise ScaleFormatError("Malformed duration representation: {}".format(representation))

        return scales

    def to_centuries(self):
        return round(self.seconds / float(SCALE_CENTURY_CONVERSION_UNIT), 2)

    def to_decades(self):
        return round(self.seconds / float(SCALE_DECADE_CONVERSION_UNIT), 2)

    def to_years(self):
        return round(self.seconds / float(SCALE_YEAR_CONVERSION_UNIT), 2)

    def to_months(self):
        return round(self.seconds / float(SCALE_MONTH_CONVERSION_UNIT), 2)

    def to_weeks(self):
        return round(self.seconds / float(SCALE_WEEK_CONVERSION_UNIT), 2)

    def to_days(self):
        return round(self.seconds / float(SCALE_DAY_CONVERSION_UNIT), 2)

    def to_hours(self):
        return round(self.seconds / float(SCALE_HOUR_CONVERSION_UNIT), 2)

    def to_minutes(self):
        return round(self.seconds / float(SCALE_MINUTE_CONVERSION_UNIT), 2)

    def to_seconds(self):
        return round(self.seconds / float(SCALE_SECOND_CONVERSION_UNIT), 2)

    def to_miliseconds(self):
        return round(self.seconds / float(SCALE_MILISECOND_CONVERSION_UNIT), 2)

