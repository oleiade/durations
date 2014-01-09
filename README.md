durations
=========

## What it is?

A python durations parsing library, providing a straight forward api to parse durations string representations
such as '1d' or '1 day 2 hours' or '2 days 3h 26m 52s' and convert them to numeric value.

## Why is it?

It's easier, and more straight forward to read a duration in it's human form (at least for a human), as an expression
rather than an amount. When writing configuration files for example:

```yaml
interval: 3 hours
```

is easier to understand for a human than

```yaml
interval: 10800  # seconds
```

right?

## Installation

### with pip

```bash
$ pip install durations
```

### with setuptools

```bash
$ git clone git@github.com:oleiade/durations
$ cd durations
$ python setup.py install
```

## Usage

To parse a duration string representation, just instantiate a Duration object, and let it work for you.
A Duration representation is composed of as many ``<value><scale>`` pairs as you need to express it:
* A value is an integer amount.
* A scale is a duration unit in it's short or long form (both singular and plural).
* Duration pairs can be separated with sep characters and expressions such as "," or "and"

*examples*:

```
1d
2 days
2 days and 4 hours
4M, 22d and 6hours
...
```

#### Scales reference

```
Century scale formats: 'c', 'century', 'centuries'
Decade scale formats: 'D', 'decade', 'decades'
Year scale formats: 'y', 'year', 'Year'
Month scale formats: 'M', 'month', 'months'
Week scale formats: 'w', 'week', 'weeks'
Day scale formats: 'd', 'day', 'days'
Hour scale formats: 'h', 'hour', 'hours'
Minute scale formats:'m', 'minute', 'minutes'
Second scale formats: 's', 'second', 'seconds'
Milisecond scale formats: 'ms', 'milisecond', 'miliseconds'
```

#### A good example worths it all

```python
>>> from durations import Duration

>>> one_hour = '1hour'

>>> one_hour_duration = Duration(one_hour)
>>> one_hour_duration.to_seconds()
3600.0
>>> one_hour_duration.to_minutes()
60.0


# You can even compose durations in their short
# and long variations
>>> two_days_three_hours = '2 days, 3h'
>>> two_days_three_hours_duration = Duration(two_days_three_hours)
>>> two_days_three_hours_duration.to_seconds()
183600.0
>>> two_days_three_hours_duration.to_hours()
51.0
```


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/oleiade/durations/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

