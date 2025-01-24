"""
Module to initialize sentry if used
"""

from logging import getLogger

_logger = getLogger(__name__)


class Sentry:
    """
    Sentry remote logging class
    :param str dsn: Sentry dsn
    :param str env: Sentry env, default: dev
    :returns: None
    """

    def __init__(self, dsn: str, env: str = "dev") -> None:
        """ """
        try:
            import sentry_sdk

            _logger.debug("Initializing sentry")
            sentry_sdk.init(dsn=dsn, environment=env)
        except ImportError:
            pass
