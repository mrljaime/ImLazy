# --*-- encoding: utf-8 --*--

import logging
from config import config

# Starting with configuration
filename = "%s/%s" % (
    config.get("stamper", "logging-path"),
    config.get("stamper", "logging-file")
)

level = logging.DEBUG

if "DEBUG" == str(config.get("stamper", "logging-level")):
    level = logging.DEBUG

if "INFO" == str(config.get("stamper", "logging-level")):
    level = logging.INFO

logging.basicConfig(filename=filename, filemode="w", format="%(asctime)s %(message)s", level=level) 
