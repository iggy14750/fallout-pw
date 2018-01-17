
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

if __name__ == '__main__':
    unittest.main()
