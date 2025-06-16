import unittest
import Game

class MyTestCase(unittest.TestCase):

    def test_game(self):
        game = Game.Game()
        input = [4, 3, 2, 1]
        self.assertEqual(game.entry(input), True)

    def test_game_false(self):
        game = Game.Game()
        input = [4, 3, 1]
        self.assertEqual(game.entry(input), False)

if __name__ == '__main__':
    unittest.main()
