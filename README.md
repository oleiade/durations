durations
=========

A python durations parsing library. It allows to parse durations string representation such as '1d' or '1day' or '2 days' to
a numeric value. As a default every value will be parsed as a second amount, but duration objects expose an api to convert
this amount to any unit you may want: minutes, hours, years, centuries...

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
A Duration representation is formatted like : ``<value><scale>``. A value is an integer amount. A scale
is a duration unit in it's short or long form (both singular and plural).

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
>>> two_days = '2days'

>>> one_hour_duration = Duration(one_hour)
>>> one_hour_duration.to_seconds()
3600.0
>>> one_hour_duration.to_minutes()
60.0

>>> two_days_duration = Duration(two_days)
>>> two_days_duration.to_hours()
48.0
>>> two_days_duration.to_seconds()
172800.0
```
