import pytest

if __name__ == "__main__":
    status = pytest.main(["-x", "tests", "-v"])
    exit(status)
