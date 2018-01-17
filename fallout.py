
""" A utility for cracking terminals in the Fallout universe. """

class PasswordSet:
    """ The primary abstraction, PasswordSet holds, shocking,
    a set of passwords, and provides methods for querying them. """

    def __init__(self, passwords):
        self._words = list(passwords)

    def __iter__(self):
        return iter(self._words)


if __name__ == '__main__':
    pass
