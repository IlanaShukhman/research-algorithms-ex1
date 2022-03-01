from unittest import TestCase
import question3

class Test(TestCase):
    def test_find_root(self):
        self.assertTrue(1.9 <= question3.find_root(lambda x: x ** 2 - 4, 1, 5) <= 2.1)
        def f(x: int):
            return 2 * x
        self.assertTrue(-0.1 <= question3.find_root(f, -1, 1) <= 0.1)
        def f1(x: int):
            return x**2 + 2*x +1
        self.assertTrue(-1.1 <= question3.find_root(f1, -10, 10) <= -0.9)