
""" Tests for fallout.py """

import unittest
import fallout

class TestFunctions(unittest.TestCase):
    """ Testing out a functional approach now. """

    def test_shared_same_word(self):
        """ All letters are shared between two copies of the same word. """
        word = 'string'
        self.assertEqual(fallout.shared(word, word), len(word))

    def test_shared_same_len(self):
        """ 3 letters are shared between 'love', and 'lode'. """
        self.assertEqual(3, fallout.shared('love', 'lode'))

    def test_shared_different_len(self):
        """ 3 letters are shared between 'disco' and 'Tisc'."""
        self.assertEqual(3, fallout.shared('disco', 'Tisc'))

    def test_best_first_element(self):
        """ The best element of this list is the first one. """
        words = ['fire', 'ford', 'kirk']
        self.assertEqual(words[0], fallout.best(words))

    def test_best_single_element(self):
        """ The best element of a signleton is the element. """
        word = 'this'
        self.assertEqual(word, fallout.best([word]))

    def test_best_second_elem(self):
        """ The best element of this list is second. """
        words = ['rimir', 'rumor', 'yuyoy']
        self.assertEqual(words[1], fallout.best(words))

    def test_filter_empty_iterable(self):
        """ Nothing in, nothing out. """
        self.assertEqual([], list(fallout.filter_shares([], 'word', 2)))

    def test_filter_all_survive(self):
        """ All elements will match the criteria. """
        iterable = ['TndTT', 'uTTTnT', 'unT']
        word = 'undone'
        self.assertEqual(iterable, list(fallout.filter_shares(iterable, word, 2)))

    def test_filter_none_survive(self):
        """ No elements will match criteria. """
        word = 'yourself'
        # match too many, match too few, wrong position
        iterable = ['yourself', 'nothing', 'TyouTTT']
        self.assertEqual([], list(fallout.filter_shares(iterable, word, 3)))


if __name__ == '__main__':
    unittest.main()
