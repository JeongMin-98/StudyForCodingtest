from borg import Borg


def main():
    """
    >>> class ABorg(Borg): pass
    >>> class BBorg(Borg): pass
    >>> class A1Borg(ABorg): pass
    >>> a = ABorg()
    >>> a1 = A1Borg()
    >>> b = BBorg()
    >>> a.num = 100
    >>> a.num
    >>> a1.num
    >>> b.num
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
