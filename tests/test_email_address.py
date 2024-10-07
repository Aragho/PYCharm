import unittest

import email_address





class TestEmailAddress(unittest.TestCase):
    def test_that_the_function_exists(self):
        email_address.validate_email_address("email")

    def test_that_validate_email_address(self):
        email = "Oluwadanny19@gmail.com"
        actual = email_address.validate_email_address(email)
        self.assertTrue(actual)
    def test_that_validate_email_address_without_one(self):
        email = "Oluwadanny19.gmail.com"
        actual = email_address.validate_email_address(email)
        self.assertFalse(actual)



