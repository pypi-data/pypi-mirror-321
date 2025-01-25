import unittest
from textutils.core import extract_emails, validate_url

# Test suite for core utility functions in textutils
class TestCore(unittest.TestCase):

    # Test extract_emails functionality
    def test_extract_emails(self):
        text = "Contact us at test@example.com and support@domain.org"
        emails = extract_emails(text)
        self.assertEqual(emails, ['test@example.com', 'support@domain.org'])

    # Test validate_url functionality
    def test_validate_url(self):
        self.assertTrue(validate_url("https://example.com"))
        self.assertFalse(validate_url("htp://invalid-url"))

if __name__ == "__main__":
    unittest.main()
