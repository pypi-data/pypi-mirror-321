"""
Module for check functions
"""

import json
import sys
import time
from logging import getLogger

from tabulate import tabulate

from gnt_monitoring.constants import NAGIOS_STATUS_CODES
from gnt_monitoring.helpers import check_for_status, convert_to_human
from gnt_monitoring.rapi import GntMonitoring

_logger = getLogger(__name__)


async def memory_check(
    cluster: GntMonitoring, warning: int, critical: int, check_field: str
) -> None:
    """
    Memory monitoring function
    :param float warning: percentage at which return warning
    :param float critical: percentage at which return critical
    """
    monitoring_data = {}
    start = time.perf_counter()
    hosts = await cluster.hosts()
    hosts = [h["id"] for h in hosts]
    for host in hosts:
        host_memory = await cluster.host_memory(host=host)
        _logger
        value = host_memory[check_field]
        if check_field == "free":
            _logger.debug("Inverting values for checking")
            warning = -abs(warning)
            critical = -abs(critical)
            value = -abs(host_memory[check_field])
        host_memory["status"] = check_for_status(
            warning=warning, critical=critical, value=value
        )
        _logger.debug(f"Memory data:\n{json.dumps(host_memory, indent=2)}")
        monitoring_data[host] = host_memory
    end = time.perf_counter()
    exec_time = round(end - start, 2)
    _logger.debug(f"Collecting data took: {exec_time}")
    process_results(monitoring_data)


def process_results(data: dict) -> None:
    """
    Process gathered results
    :param dict data: data collected from rapi
    :return: None
    """
    overal_status = max([s["status"] for _, s in data.items()])
    output = [["Host", "Status", "Usage %", "Total", "Allocated", "Used", "Available"]]
    for host, info in data.items():
        host_line = []
        host_line.append(host)
        status_converted = NAGIOS_STATUS_CODES.get(info["status"])
        host_line.append(status_converted)
        host_line.append(info["allocated_perc"])
        total = convert_to_human(info["total"])
        host_line.append(f"{total[0]} {total[1]}")
        allocated = convert_to_human(info["allocated"])
        host_line.append(f"{allocated[0]} {allocated[1]}")
        used = convert_to_human(info["used"])
        host_line.append(f"{used[0]} {used[1]}")
        free = convert_to_human(info["free"])
        host_line.append(f"{free[0]} {free[1]}")
        output.append(host_line)
    print(tabulate(output, tablefmt="simple", headers="firstrow", numalign="center"))
    sys.exit(overal_status)
