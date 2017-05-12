import unittest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class FactorialTests(unittest.TestCase):
    def test_factorial_of_zero(self):
        fac = factorial(0)
        self.assertEqual(fac, 1)
        # self.assertTrue(fac == 2)

    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)

    def casual_method(self):
        pass

    def test_failing(self):
        a = 2
        b = 3
        self.assertEqual(2+2, 5)

    def test_failing_2(self):
        self.assertEqual(3+3, 7)

    def test_raises_error(self):
        with self.assertRaises(ValueError):
            pass
            # raise ValueError
            print('with after')
        print('after')


class SetupTests(unittest.TestCase):
    def test_one(self):
        print('one')

    def test_two(self):
        print('two')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

