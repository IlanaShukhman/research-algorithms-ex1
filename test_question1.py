from unittest import TestCase
import question1


class Test(TestCase):
    #define some functions:
    def f1(x:int):
        return x+2
    def f2(x, y, z:float):
        return x*y-z
    def f3():
        return 14

    def test_safe_call(self):
        #simple tests
        self.assertEqual(question1.safe_call(Test.f1, x=5) , 7)
        self.assertEqual(question1.safe_call(Test.f2, x=5, y=8, z=-1.0), 41.0)
        self.assertEqual(question1.safe_call(Test.f3), 14)

        #throw exception
        self.assertRaises(Exception, question1.safe_call(Test.f1, x=5))
        self.assertRaises(Exception, question1.safe_call(Test.f2, x=5, y = 25, z = 12))
