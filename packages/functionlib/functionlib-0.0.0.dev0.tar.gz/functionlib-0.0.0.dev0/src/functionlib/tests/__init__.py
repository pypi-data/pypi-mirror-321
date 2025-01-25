import unittest

__all__ = ["test"]


def test() -> unittest.TextTestRunner:
    "This function runs all the tests."
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir="functionlib.tests")
    runner = unittest.TextTestRunner()
    result = runner.run(tests)
    return result
