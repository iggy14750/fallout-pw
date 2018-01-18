
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









class TestPasswordSet(unittest.TestCase):
    """ Pretty self-explanatory. """
    def test_constructor(self):
        """For lint"""
        self.assertIsNotNone(fallout.PasswordSet(
            ['One', 'Two', 'Three']
        ))

    def test_iterator(self):
        """ Test that this object outputs the same objects in an iterator."""
        words = {'one', 'two', 'three'}
        self.assertEqual(words, set(fallout.PasswordSet(words)))

    def test_best_single_element(self):
        """ Initializing a PasswordSet with a single element will make that element the best. """
        self.assertEqual('single', fallout.PasswordSet(['single']).best())

    def test_best_first_element(self):
        """ The best of this list happens to be the first one. """
        words = ['fire', 'ford', 'kirk']
        self.assertEqual(words[0], fallout.PasswordSet(words).best())

    def _test_best_not_first_element(self):
        """ Now the best element is the second one. """
        words = ['rimir', 'rumor', 'yuyoy']
        self.assertEqual(words[1], fallout.PasswordSet(words).best())


if __name__ == '__main__':
    unittest.main()
