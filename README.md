import auto for Python
----------------------

Automatic importer for Python libraries.

Example usage:

    $ python3
    >>> import auto
    >>> auto.math.pi
    3.141592653589793
    >>> list(auto.itertools.combinations(range(1,6),2))
    [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

    >>> from auto import *
    >>> math.exp(1)
    2.718281828459045
    >>> math.sqrt(2)
    1.4142135623730951
    >>> pot=functools.partial(operator.__pow__,2)
    >>> pot(6)
    64
    >>> pot(16)
    65536
    >>> http.server.HTTPServer
    <class 'http.server.HTTPServer'>
    >>> 
    >>> print(autos())
    import functools
    import http
    import http.server
    import itertools
    import math
    import operator
    >>> 

Version
-------

Version 0.0

* Python 3 only.
* imports for most standard libraries
