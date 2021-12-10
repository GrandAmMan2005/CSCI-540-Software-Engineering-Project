from unittest import TestCase
from Database import passwordCheck
from Database import getBalance
from Database import creatingAccount



class Test(TestCase):
    def test_password_check(self):
        result = passwordCheck("pass1", "pass2")
        self.assertFalse(result)
        result1 = passwordCheck("pass1", "pass1")
        self.assertTrue(result1)

    def test_get_balance(self):
        result = getBalance("test")
        self.assertEqual(result, 1000)
        result1 = getBalance("admin")
        self.assertEqual(result1, 2000)
