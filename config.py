# --*-- encodinf: utf-8 --*--
"""
Just defining config parser
"""

import ConfigParser
import os

config = ConfigParser.RawConfigParser()
config.read("config/app.ini")
