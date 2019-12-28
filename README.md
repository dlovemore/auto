import auto for Python
----------------------

Automatic importer for Python libraries.

Usage: 
    $ python3
    >>> import auto
    >>> auto.math.pi
    3.141592653589793
    >>> list(auto.itertools.combinations(range(1,6),2))
    [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    >>> auto.http.server
    Importer('http.server')
    >>> dir(_)
    ['BaseHTTPRequestHandler', 'CGIHTTPRequestHandler', 'DEFAULT_ERROR_CONTENT_TYPE', 'DEFAULT_ERROR_MESSAGE', 'HTTPServer', 'HTTPStatus', 'SimpleHTTPRequestHandler', 'ThreadingHTTPServer', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_url_collapse_path', 'copy', 'datetime', 'email', 'executable', 'html', 'http', 'io', 'mimetypes', 'nobody', 'nobody_uid', 'os', 'partial', 'posixpath', 'select', 'shutil', 'socket', 'socketserver', 'sys', 'test', 'time', 'urllib']
    >>> from auto import *
    >>> math.exp(1)
    2.718281828459045
    >>> dir(curses.ascii)
    ['ACK', 'BEL', 'BS', 'CAN', 'CR', 'DC1', 'DC2', 'DC3', 'DC4', 'DEL', 'DLE', 'EM', 'ENQ', 'EOT', 'ESC', 'ETB', 'ETX', 'FF', 'FS', 'GS', 'HT', 'LF', 'NAK', 'NL', 'NUL', 'RS', 'SI', 'SO', 'SOH', 'SP', 'STX', 'SUB', 'SYN', 'TAB', 'US', 'VT', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_ctoi', 'alt', 'ascii', 'controlnames', 'ctrl', 'isalnum', 'isalpha', 'isascii', 'isblank', 'iscntrl', 'isctrl', 'isdigit', 'isgraph', 'islower', 'ismeta', 'isprint', 'ispunct', 'isspace', 'isupper', 'isxdigit', 'unctrl']
    >>> 
