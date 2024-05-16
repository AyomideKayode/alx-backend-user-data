#!/usr/bin/env python3

""" Module for filtering sensitive data
This module provides a logger with redaction for sensitive data.
The module defines a RedactingFormatter class.
This formatter is used to redact sensitive data.
Example usage:
    logger = get_logger()
    logger.info("User logged in: name=john, email=john@example.com")
We define a list of fields to redact, PII_FIELDS.
Contains a get_logger() function that returns a logger object.
"""

import logging
import re
from typing import List

# Define PII_FIELDS constant with fields to be considered as PII
# Personal Identifiable Information (PII) fields, in other words sensitive
PII_FIELDS = ('name', 'password', 'email', 'ssn', 'phone')


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    This class will redact sensitive data from log messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialize the RedactingFormatter object
        Arguments:
          fields -- list of strings representing fields to obfuscate
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        # Initialize the fields attribute with the provided list of fields
        self.fields = fields if fields is not None else []

    def format(self, record: logging.LogRecord) -> str:
        """ Format the log record
        By first calling the format() method of the parent class, we can
        obtain the original log message.
        We then call the filter_datum() function to obfuscate the sensitive
        data in the log message.
        Arguments:
          record -- log record to format
        Returns:
        The formatted log message.
        """
        original_message = super(RedactingFormatter, self).format(record)
        filtered_data = filter_datum(
            self.fields, self.REDACTION, original_message, self.SEPARATOR)
        return filtered_data


def get_logger() -> logging.Logger:
    """ Get a logger object
    Returns:
    A logging.Logger object.
    """
    logger = logging.getLogger('user_data')  # Create a logger object
    logger.setLevel(logging.INFO)  # Set the logger level to INFO
    logger.propagate = False  # Prevent the log messages from being propagated

    # Add a console handler to the logger
    console_handler = logging.StreamHandler()

    # Set the formatter of the console handler to a RedactingFormatter object
    formatter = RedactingFormatter(PII_FIELDS)
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)
    return logger
