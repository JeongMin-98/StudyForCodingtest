from borg import Borg


def main():
    """
    >>> class ABorg(Borg): pass
    >>> class BBorg(Borg): pass
    >>> class A1Borg(ABorg): pass
    >>> a = ABorg()
    >>> a1 = A1Borg()
    >>> b = BBorg()
    >>> a.x = 100
    >>> a.x
    >>> a1.x
    >>> b.x
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
