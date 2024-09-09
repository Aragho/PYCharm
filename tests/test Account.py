from classAccountPractice import Account
from unittest import TestCase
from decimal import Decimal


class TestAccount(TestCase):
    def test_that_account_can_deposit(self):
        a1 = Account("john", "0000")
        a1.deposit(10000)
        self.assertEqual(a1.balance, 10000)

