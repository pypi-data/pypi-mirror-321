# International Distributed Systems Corporation (IDSC)
# Copyright 2025

import sys

if sys.version_info[:2] < (3, 9):
    raise RuntimeError("This version of distributed-systems requires at least Python 3.9")
if sys.version_info[:2] >= (3, 14):
    raise RuntimeError("This version of distributed-systems does not support Python 3.14+")

__version__ = "0.1.0"
