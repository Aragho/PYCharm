import unittest
from math import expm1

import loanContract
from loanContract import LoanContract


class TestForLoanContract(unittest.TestCase):
    def test_that_the_function_exist(self):
        loan = LoanContract("Princess Ademoye", 2,100,3 )

    def test_that_the_there_is_data_properties(self,):
        loan_contract = LoanContract("Princess Ademoye", 2,100,3)
        actual = str (loan_contract)
        expected = f"""
            name: Princess Ademoye
            interest_rate: 2
            loan_amount: 100
            loan_period: 3
            """
        self.assertEqual(actual,expected)
    
    def test_that_the_monthly_payment_has_being_recieved(self):
        loan_contract = LoanContract("Princess Ademoye", 2,100,2)
        expected = loan_contract.compute_monthly_payment()
        actual = 17.09
        self.assertEqual(actual,expected)
        self.assertEqual(410.16, loan_contract.compute_total_payment())

