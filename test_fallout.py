
""" Tests for fallout.py """

import unittest
import fallout

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

if __name__ == '__main__':
    unittest.main()
