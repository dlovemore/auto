# >>> import auto
# >>> webbrowser
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'webbrowser' is not defined
# >>> auto.webbrowser
# Importer('webbrowser')
# >>> dir(auto.webbrowser)
# ['BackgroundBrowser', 'BaseBrowser', 'Chrome', 'Chromium', 'Elinks', 'Error', 'Galeon', 'GenericBrowser', 'Grail', 'Konqueror', 'Mozilla', 'Netscape', 'Opera', 'UnixBrowser', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_browsers', '_lock', '_os_preferred_browser', '_synthesize', '_tryorder', 'get', 'main', 'open', 'open_new', 'open_new_tab', 'os', 'register', 'register_X_browsers', 'register_standard_browsers', 'shlex', 'shutil', 'subprocess', 'sys', 'threading']
# >>> auto.webbrowser.os
# <module 'os' from '/usr/lib/python3.7/os.py'>
# >>> auto.xml
# Importer('xml'('etree', 'ElementTree')('dom', 'minidom', 'pulldom')('sax', 'handler', 'saxutils', 'xmlreader')('parsers', 'expat'))
# >>> auto.xml.etree
# Importer('xml.etree''ElementTree')
# >>> auto.xml.etree.ElementTree
# Importer('xml.etree.ElementTree')
# >>> 
# >>> dir(_)
# ['Comment', 'Element', 'ElementPath', 'ElementTree', 'HTML_EMPTY', 'PI', 'ParseError', 'ProcessingInstruction', 'QName', 'SubElement', 'TreeBuilder', 'VERSION', 'XML', 'XMLID', 'XMLParser', 'XMLPullParser', '_Element_Py', '_ListDataStream', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_escape_attrib', '_escape_attrib_html', '_escape_cdata', '_get_writer', '_namespace_map', '_namespaces', '_raise_serialization_error', '_sentinel', '_serialize', '_serialize_html', '_serialize_text', '_serialize_xml', 'collections', 'contextlib', 'dump', 'fromstring', 'fromstringlist', 'io', 'iselement', 'iterparse', 'parse', 're', 'register_namespace', 'sys', 'tostring', 'tostringlist', 'warnings']
# >>> auto.xml.etree.ElementTree.Element
# <class 'xml.etree.ElementTree.Element'>
# >>> auto.xml.etree.ElementPath
# <module 'xml.etree.ElementPath' from '/usr/lib/python3.7/xml/etree/ElementPath.py'>
# >>> 
# >>> auto.autos()
# 'import webbrowser\nimport xml\nimport xml.etree'
# >>> 
# >>> from auto import *
# >>> http
# Importer('http''server''cookies''cookiejar')
# >>> http.server
# Importer('http.server')
# >>> http.cookies
# Importer('http.cookies')
# >>> dir(_)
# ['BaseCookie', 'CookieError', 'Morsel', 'SimpleCookie', '_CookiePattern', '_LegalChars', '_LegalKeyChars', '_LegalValueChars', '_OctalPatt', '_QuotePatt', '_Translator', '_UnescapedChars', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_getdate', '_is_legal_key', '_monthname', '_nulljoin', '_quote', '_semispacejoin', '_spacejoin', '_unquote', '_weekdayname', 're', 'string']
# >>> http.cookies.SimpleCookie
# <class 'http.cookies.SimpleCookie'>
# >>> 
# >>> dir(http)
# ['HTTPStatus', 'IntEnum', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'cookiejar', 'cookies', 'server']
# >>> dir(http.server)
# ['BaseHTTPRequestHandler', 'CGIHTTPRequestHandler', 'DEFAULT_ERROR_CONTENT_TYPE', 'DEFAULT_ERROR_MESSAGE', 'HTTPServer', 'HTTPStatus', 'SimpleHTTPRequestHandler', 'ThreadingHTTPServer', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_url_collapse_path', 'copy', 'datetime', 'email', 'executable', 'html', 'http', 'io', 'mimetypes', 'nobody', 'nobody_uid', 'os', 'partial', 'posixpath', 'select', 'shutil', 'socket', 'socketserver', 'sys', 'test', 'time', 'urllib']
# >>> hasattr(http,'x')
# False
# >>> hasattr(http.server,'x')
# False
# >>> hasattr(math,'x')
# False
# >>> hasattr(math,'pi')
# True
# >>> 
# >>> math.pi
# 3.141592653589793
# >>> 
# >>> import http
# >>> 
# >>> 
# >>> math.pi
# 3.141592653589793
# >>> math
# Importer('math')
# >>> dir(math)
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
# >>> autos()
# 'import http\nimport math\nimport webbrowser\nimport xml\nimport xml.etree'
# >>> dir(itertools)
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', '_grouper', '_tee', '_tee_dataobject', 'accumulate', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 'cycle', 'dropwhile', 'filterfalse', 'groupby', 'islice', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 'tee', 'zip_longest']
# >>> itertools
# Importer('itertools')
# >>> list(itertools.combinations(range(1,6),2))
# [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
# >>> print(autos())
# import http
# import itertools
# import math
# import webbrowser
# import xml
# import xml.etree
# >>> dir(pprint)
# ['PrettyPrinter', '_StringIO', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_builtin_scalars', '_collections', '_perfcheck', '_recursion', '_safe_key', '_safe_repr', '_safe_tuple', '_sys', '_types', '_wrap_bytes_repr', 'isreadable', 'isrecursive', 'pformat', 'pprint', 're', 'saferepr']
# >>> autos()
# 'import http\nimport itertools\nimport math\nimport webbrowser\nimport xml\nimport xml.etree'
# >>> 
# >>> 
# >>> tkinter.ttk
# Importer('tkinter.ttk')
# >>> 
