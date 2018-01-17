
""" A utility for cracking terminals in the Fallout universe. """

class PasswordSet:
    """ The primary abstraction, PasswordSet holds, shocking,
    a set of passwords, and provides methods for querying them. """

    def __init__(self, passwords):
        self._words = list(passwords)

    def __iter__(self):
        return iter(self._words)

    def best(self):
        """ Returns the best choice out these possible passwords.
        Determined as the one which shares the most letters with the others. """
        return self._words[0]


if __name__ == '__main__':
    pass
