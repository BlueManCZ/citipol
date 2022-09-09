"""
Main script for starting unit tests
"""

import sys
import pytest

if __name__ == "__main__":
    status = pytest.main(["-x", "tests", "-v"])
    sys.exit(status)
