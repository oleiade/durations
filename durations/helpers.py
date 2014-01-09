from durations import Duration
from durations.exceptions import ScaleFormatError


def valid_duration(representation):
    try:
        Duration(representation)
    except ScaleFormatError:
        return False

    return True

