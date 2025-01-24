"""
Script erntry point
"""

import asyncio
import json
import sys

# from argparse import Namespace
from logging import getLogger

from gnt_monitoring._decorators import argument, command
from gnt_monitoring.arguments import base_args
from gnt_monitoring.checks import memory_check
from gnt_monitoring.constants import NAGIOS_STATUS_CODES
from gnt_monitoring.helpers import check_for_status, conver_size, convert_to_human
from gnt_monitoring.logger import init_logger
from gnt_monitoring.rapi import GntMonitoring, init_gnt_monitoring
from gnt_monitoring.sentry import Sentry

args = base_args()

subparser = args.add_subparsers(dest="subcommand")
_logger = getLogger(__name__)


@command(
    [
        argument(
            "-w",
            "--warning",
            help="Percent value for warning, default: %(default)s",
            default=75,
            type=float,
        ),
        argument(
            "-c",
            "--critical",
            help="Percent value for critical, default: %(default)s",
            default=90,
            type=float,
        ),
        argument("-W", "--warning-size", help="Warning size", type=str),
        argument("-C", "--critical-size", help="Critical size", type=str),
    ],
    parent=subparser,  # type: ignore
)
def node_memory(cluster: GntMonitoring, pargs: dict) -> None:
    """
    Main check command
    """
    if bool(pargs.get("warning_size")) or bool(pargs.get("critical_size")):
        if not bool(pargs.get("warning_size")):
            _logger.error("Warning size not provided")
            sys.exit(4)
        if not bool(pargs.get("critical_size")):
            _logger.error("Critical size not provided")
            sys.exit(4)
        warning = conver_size(pargs["warning_size"])
        critical = conver_size(pargs["critical_size"])
        if critical >= warning:
            _logger.error("Warning value can't be equal or less then critical")
            sys.exit(4)
        field_to_check = "free"
    else:
        if pargs["warning"] >= pargs["critical"]:
            _logger.error("Warning value can't be equal or higher then critical")
            sys.exit(5)
        warning = pargs.get("warning")
        critical = pargs.get("critical")
        field_to_check = "allocated_perc"
    asyncio.run(memory_check(cluster, warning, critical, field_to_check))


@command(
    [
        argument(
            "-w",
            "--warning",
            help="Warning value for nodes available, default: %(default)s",
            default=1.10,
            type=float,
        ),
        argument(
            "-c",
            "--critical",
            help="Critical value for nodes available, defailt: %(default)s",
            default=1.05,
            type=float,
        ),
    ],
    parent=subparser,  # type: ignore
)
def cluster_memory(cluster: GntMonitoring, pargs: dict) -> None:
    """
    Cli command to calculate total cluster memory
    """
    hosts = asyncio.run(cluster.hosts())
    _logger.debug(json.dumps(hosts, indent=2, default=str))
    results = {
        "total": 0,
        "allocated": 0,
        "used": 0,
        "biggest node": 0,
        "nodes available": 0.0,
        "available": 0,
    }
    results = dict(sorted(results.items()))
    key_length = 0
    for k in results.keys():
        key_length = max(key_length, len(k))
    for h in hosts:
        host = asyncio.run(cluster.host_memory(h["id"]))
        results["biggest node"] = max(results["biggest node"], host["total"])
        results["total"] += host["total"]
        results["allocated"] += host["allocated"]
        results["used"] += host["used"]
    results["available"] = results["total"] - results["allocated"]
    results["nodes available"] = round(
        results["available"] / results["biggest node"], 2
    )
    status = check_for_status(
        warning=-abs(pargs["warning"]),
        critical=-abs(pargs["critical"]),
        value=-abs(results["nodes available"]),
    )
    results = {"overal status": NAGIOS_STATUS_CODES.get(status)} | results
    for k, v in results.items():
        if isinstance(v, int):
            value, unit = convert_to_human(v)
            print(f"{k.capitalize():<{key_length}} : {value} {unit}")
        else:
            print(f"{k.capitalize():<{key_length}} : {v}")
    sys.exit(status)


def main() -> None:
    """
    Tool entry point
    :returns: None
    """
    parsed = args.parse_args()
    init_logger(level=parsed.log_level)

    if parsed.sentry_dsn:
        Sentry(dsn=parsed.sentry_dsn, env=parsed.sentry_env)
    cluster = init_gnt_monitoring(**parsed.__dict__)
    if parsed.subcommand is None:
        args.print_help()
        return
    try:
        parsed.func(cluster, parsed.__dict__)
    except KeyboardInterrupt:
        _logger.debug("Keyboard interrupt")
        sys.exit(4)
