import unittest

from assertfunction.core import assertfunction


class TestAssertFunction(unittest.TestCase):

    def test_single_argument(self):
        """Test assertfunction with a single argument."""
        try:
            assertfunction(True)  # Should pass without error
        except AssertionError:
            self.fail("assertfunction(True) raised AssertionError unexpectedly!")

        with self.assertRaises(AssertionError):
            assertfunction(False)  # Should raise AssertionError

    def test_two_arguments(self):
        """Test assertfunction with two arguments (check, message)."""
        try:
            assertfunction(
                True, "This should not raise an error"
            )  # Should pass without error
        except AssertionError:
            self.fail("assertfunction(True, ...) raised AssertionError unexpectedly!")

        with self.assertRaises(AssertionError) as cm:
            assertfunction(False, "Custom error message")  # Should raise AssertionError

        self.assertEqual(str(cm.exception), "Custom error message")

    def test_invalid_argument_count(self):
        """Test assertfunction with invalid number of arguments."""
        with self.assertRaises(Exception):
            assertfunction(True, "Message", "Extra argument")  # Too many arguments


if __name__ == "__main__":
    unittest.main()
