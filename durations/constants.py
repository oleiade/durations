from collections import namedtuple

# Scales separator chars and tokens
SEPARATOR_CHARACTERS = (
        " ",
        "\t",
        ","
)

SEPARATOR_TOKENS = (
    'and',
)

# Scale parsing tokens definition
SCALE_TOKEN_ALPHA = 0
SCALE_TOKEN_DIGIT = 1


ScaleRepresentation = namedtuple(
    'ScaleRepresentation',
    ['short', 'long_singular', 'long_plural']
)

# Duration scales string representations
SCALE_CENTURY = ScaleRepresentation('c', 'century', 'centuries')
SCALE_DECADE = ScaleRepresentation('D', 'decade', 'decades')
SCALE_YEAR = ScaleRepresentation('y', 'year', 'Year')
SCALE_MONTH = ScaleRepresentation('M', 'month', 'months')
SCALE_WEEK = ScaleRepresentation('w', 'week', 'weeks')
SCALE_DAY = ScaleRepresentation('d', 'day', 'days')
SCALE_HOUR = ScaleRepresentation('h', 'hour', 'hours')
SCALE_MINUTE = ScaleRepresentation('m', 'minute', 'minutes')
SCALE_SECOND = ScaleRepresentation('s', 'second', 'seconds')
SCALE_MILISECOND = ScaleRepresentation('ms', 'milisecond', 'miliseconds')

# Conversion constants. Each contains it's seconds
# per unit amount. For example: 1 minute is 60 seconds,
# or 1 hour is 3600 seconds.
SCALE_SECOND_CONVERSION_UNIT = 1
SCALE_MILISECOND_CONVERSION_UNIT = 0.001 * SCALE_SECOND_CONVERSION_UNIT
SCALE_MINUTE_CONVERSION_UNIT = 60 * SCALE_SECOND_CONVERSION_UNIT
SCALE_HOUR_CONVERSION_UNIT = 60 * SCALE_MINUTE_CONVERSION_UNIT
SCALE_DAY_CONVERSION_UNIT = 24 * SCALE_HOUR_CONVERSION_UNIT
SCALE_WEEK_CONVERSION_UNIT = 7 * SCALE_DAY_CONVERSION_UNIT
SCALE_MONTH_CONVERSION_UNIT = 30.5 * SCALE_DAY_CONVERSION_UNIT  # Ugly hack: feel free to enhance
SCALE_YEAR_CONVERSION_UNIT = 12 * SCALE_MONTH_CONVERSION_UNIT
SCALE_DECADE_CONVERSION_UNIT = 10 * SCALE_YEAR_CONVERSION_UNIT
SCALE_CENTURY_CONVERSION_UNIT = 10 * SCALE_DECADE_CONVERSION_UNIT


