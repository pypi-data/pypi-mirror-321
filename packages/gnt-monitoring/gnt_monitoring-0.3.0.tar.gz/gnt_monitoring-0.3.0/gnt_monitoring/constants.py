"""
Constant module
"""

from enum import Enum

DEFAULT_LOG_FORMAT = "%(asctime)s %(levelname)s - %(message)s"
NAGIOS_STATUS_CODES = {0: "OK", 1: "WARNING", 2: "CRITICAL", 3: "UNKNOWN"}


class units(Enum):
    MB = 1
    GB = 1000
    TB = 1000000
    M = 1
    G = 1000
    T = 1000000
    MIB = 1
    GIB = 1024
    TIB = 1048576
