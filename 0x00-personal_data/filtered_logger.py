#!/usr/bin/env python3

""" Module for filtering sensitive data
This module provides a logger with redaction for sensitive data.
The module defines a RedactingFormatter class.
This formatter is used to redact sensitive data.
Example usage:
    logger = get_logger()
    logger.info("User logged in: name=john, email=john@example.com")
"""

import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
    Filter sensitive data in a message.
    Arguments:
      fields -- list of strings representing fields to obfuscate
      redaction -- string to replace field values with
      message -- log line string
      separator -- character separating fields in the log line
    Returns:
    The obfuscated log message.
    """
    # Create a regular expression pattern to match the fields to be redacted
    pattern = '|'.join(f'{field}=[^{separator}]*' for field in fields)

    # Use the re.sub() function to replace the matched fields
    # with the redaction string
    # The lambda function is used to split the matched field and replace only
    # the value with the redaction string
    filtered_data = re.sub(
        pattern, lambda m: f"{m.group().split('=')[0]}={redaction}", message)
    return filtered_data
