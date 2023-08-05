import unittest 
import number_game

class Test_Game(unittest.TestCase):
    def test1(self):
        result = number_game.run_guess(5,5)
        self.assertTrue(result)
    
    def test2(self):
        result = number_game.run_guess(5,0)
        self.assertFalse(result)
    
    def test3(self):
        result = number_game.run_guess(5,11)
        self.assertFalse(result)
    
    def test4(self):
        result = number_game.run_guess(5,"uiii")
        self.assertFalse(result)