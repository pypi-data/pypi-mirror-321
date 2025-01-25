import datetime
import logging
import requests
import json
from ..general_utilities import get_server_url

class HTTPLogHandler(logging.Handler):
    """
    Custom logging handler to send logs to a server via HTTP.
    """

    def __init__(self, IN_DEV_MODE=False, USE_BETA_URL=False):
        super().__init__()
        server_url = get_server_url(IN_DEV_MODE, USE_BETA_URL)
        self.url = f"{server_url}/api/experiments/processSDKLogs"
        print(f"Log handler URL set to: {self.url}")

    def formatTime(self, record, datefmt=None):
        """
        Override formatTime to customize the timestamp format.
        """
        ct = datetime.datetime.fromtimestamp(record.created)
        if datefmt:
            return ct.strftime(datefmt)
        return ct.isoformat()  # Default to ISO 8601 format

    def emit(self, record):
        log_entry = self.format(record)  # Format the log record
        payload = {
            "level": record.levelname,
            "message": log_entry,
            "module": record.module,
            "funcName": record.funcName,
            "lineNo": record.lineno,
            "timestamp": self.formatTime(record),
        }
        try:
            response = requests.post(self.url, json=payload, timeout=5)
            response.raise_for_status()  # Raise an error for HTTP failures
        except requests.RequestException as e:
            # Handle errors (e.g., log them locally)
            print(f"Failed to send log to {self.url}: {e}")