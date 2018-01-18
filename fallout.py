
""" A utility for cracking terminals in the Fallout universe. """

def count(iterable, condition=None):
    """ Counts the elements of 'iterable' which meet 'condition'."""
    num = 0
    predicate = condition or (lambda x: True)
    for elem in iterable:
        if predicate(elem):
            num += 1
    return num

def shared(one, two):
    """ Returns the number of elements in these two iterables which
    are equivalent and in the same position. """
    return count(zip(one, two), lambda tup: tup[0] == tup[1])

def best(passwords):
    """ Returns the element of 'passwords' which shares the most characters
    with the other elements. """
    winner = (None, 0)
    for word in passwords:
        num = 0
        for other in passwords:
            num += shared(word, other)
        if num > winner[1]:
            winner = (word, num)
    return winner[0]

def filter_shares(iterable, word, number):
    """ Filters 'iterable' down to those which share 'number' characters with 'word'."""
    return filter(
        lambda elem: shared(elem, word) == number,
        iterable
    )








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
