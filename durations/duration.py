from collections import namedtuple
from functools import partial
from types import MethodType

from durations.exceptions import ScaleFormatError
from durations.scales import Scale


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
        self.representation = self.parse(representation)

        self.value = self.representation.value
        self.scale = self.representation.scale

        self.gen_conversion_methods()

    def __str__(self):
        return '<Duration {}>'.format(self.representation)

    def __repr__(self):
        return self.__str__()

    def parse(self, representation):
        """Parses a duration string representation to a
        DurationRepresentation.

        :param  representation: duration as a string, example: '1d' (day),
                                '34minutes' (minutes), '485s' (seconds)...
        :type   representation: string

        :returns: the parsed duration representation
        :rtype: DurationRepresentation
        """
        i = 0
        value_str = ''
        scale_str = ''

        while representation[i].isdigit():
            value_str += representation[i]
            i += 1

        scale_str = representation[i:]
        scale = Scale(scale_str)

        return DurationRepresentation(float(value_str), scale)

    def to_seconds(self):
        """Convert stored duration value to seconds units"""
        return self.value * self.scale.conversion_unit

    def gen_conversion_methods(self):
        """Generate durations conversion methods

        Such as to_minutes, to_days, to_...
        """
        def convert_to(scale_representation, value=self.value):
            conversion_units = self.scale.SCALES_CONVERTION_UNITS
            conversion_unit = conversion_units[scale_representation.short]
            seconds = self.value * self.scale.conversion_unit

            return round(seconds / conversion_unit, 2)

        for scale_representation in self.scale.SCALES:
            method_name = 'to_' + scale_representation.long_plural
            conversion_method = partial(convert_to, scale_representation)
            setattr(
                self,
                method_name,
                MethodType(conversion_method, self, type(self))
            )


