import unittest
import main

class test_main(unittest.TestCase):
    def test_do_stuf(self):
        testparam=10
        result=main.do_stuf(testparam)
        self.assertEqual(result,20)
        
    def test_do_stuf(self):
        testparam='ibduoih'
        result=main.do_stuf(testparam)
        self.assertTrue(isinstance(result,ValueError))