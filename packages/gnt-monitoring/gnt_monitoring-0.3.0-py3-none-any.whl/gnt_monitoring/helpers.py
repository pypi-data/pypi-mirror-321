"""
Helper functions 
"""

import re
import sys
from logging import getLogger
from typing import Tuple, Union

from gnt_monitoring.constants import units

_logger = getLogger(__name__)


def percentage(part: int, whole: int) -> float:
    """
    Calculating percentage of a given numbers
    :param int part: Number for which to calculate percentage
    :param int whole: Whole number
    :returns: float
    """
    return round(100 * float(part) / float(whole), 2)


def convert_to_human(size: int) -> Tuple[float, str]:
    """
    Convert given size number to human readable format
    :param int size: number which must be converted
    :return: tuple of converted number rounded to 2 and unit
    """
    UNITS = ["MiB", "GiB", "TiB", "PiB"]
    for unit in UNITS:
        if unit == UNITS[-1]:
            break
        if float(size) < 1024.0:
            break
        size = round(float(size) / 1024.0, 2)
    return size, unit


def check_for_status(
    warning: Union[int, float], critical: Union[int, float], value: Union[int, float]
) -> int:
    """
    check for value status
    :param int|float warning: Warning value
    :param int|float critical: Critical value
    :param int|float value: Value to verify
    """
    if critical > value >= warning:
        return 1
    elif value >= critical:
        return 2
    return 0


def conver_size(size: str) -> int:
    """
    Validate size parameter
    """
    _, s, u = re.split("(\\d+)", size)
    if u == "":
        return s
    try:
        return int(s) * units[u.upper()].value
    except KeyError:
        _logger.error("Key %s not found", u)
        sys.exit(4)
