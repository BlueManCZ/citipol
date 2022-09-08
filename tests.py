import pytest
import sys

if __name__ == "__main__":
    status = pytest.main(["-x", "tests", "-v"])
    sys.exit(status)
