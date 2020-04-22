# >>> import auto
# >>> type(auto)
# <class 'module'>
# >>> webbrowser
# <3>:1: NameError: name 'webbrowser' is not defined
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
# >>> 
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
# >>> m=dir(math)
# >>> a=dir()
# >>> from math import *
# >>> b=dir()
# >>> set(b)-set(a)
# {'pow', 'hypot', 'ceil', 'atan', 'degrees', 'fsum', 'tanh', 'log', 'modf', 'erf', 'e', 'fmod', 'pi', 'radians', 'asinh', 'log2', 'lgamma', 'cosh', 'log10', 'floor', 'sqrt', 'frexp', 'ldexp', 'tau', 'erfc', 'isclose', 'remainder', 'fabs', 'cos', 'sin', 'atan2', 'factorial', 'isfinite', 'tan', 'isinf', 'trunc', 'gamma', 'atanh', 'asin', 'log1p', 'acosh', 'gcd', 'a', 'nan', 'copysign', 'acos', 'sinh', 'inf', 'exp', 'isnan', 'expm1'}
# >>> _^set(m)
# {'__loader__', '__doc__', '__package__', '__name__', '__spec__', 'a'}
# >>> 'a' in globals()
# True
# >>> d=dict()
# >>> 
# >>> d+math
# <auto.Importer.GWrap object at 0xb63e7650>
# >>> _.g
# {'acos': <built-in function acos>, 'acosh': <built-in function acosh>, 'asin': <built-in function asin>, 'asinh': <built-in function asinh>, 'atan': <built-in function atan>, 'atan2': <built-in function atan2>, 'atanh': <built-in function atanh>, 'ceil': <built-in function ceil>, 'copysign': <built-in function copysign>, 'cos': <built-in function cos>, 'cosh': <built-in function cosh>, 'degrees': <built-in function degrees>, 'e': 2.718281828459045, 'erf': <built-in function erf>, 'erfc': <built-in function erfc>, 'exp': <built-in function exp>, 'expm1': <built-in function expm1>, 'fabs': <built-in function fabs>, 'factorial': <built-in function factorial>, 'floor': <built-in function floor>, 'fmod': <built-in function fmod>, 'frexp': <built-in function frexp>, 'fsum': <built-in function fsum>, 'gamma': <built-in function gamma>, 'gcd': <built-in function gcd>, 'hypot': <built-in function hypot>, 'inf': inf, 'isclose': <built-in function isclose>, 'isfinite': <built-in function isfinite>, 'isinf': <built-in function isinf>, 'isnan': <built-in function isnan>, 'ldexp': <built-in function ldexp>, 'lgamma': <built-in function lgamma>, 'log': <built-in function log>, 'log10': <built-in function log10>, 'log1p': <built-in function log1p>, 'log2': <built-in function log2>, 'modf': <built-in function modf>, 'nan': nan, 'pi': 3.141592653589793, 'pow': <built-in function pow>, 'radians': <built-in function radians>, 'remainder': <built-in function remainder>, 'sin': <built-in function sin>, 'sinh': <built-in function sinh>, 'sqrt': <built-in function sqrt>, 'tan': <built-in function tan>, 'tanh': <built-in function tanh>, 'tau': 6.283185307179586, 'trunc': <built-in function trunc>}
# >>> g=globals()
# >>> 
# >>> d-math+webbrowser
# <auto.Importer.GWrap object at 0xb63e7090>
# >>> _ and _.g or _
# {'BackgroundBrowser': <class 'webbrowser.BackgroundBrowser'>, 'BaseBrowser': <class 'webbrowser.BaseBrowser'>, 'Chrome': <class 'webbrowser.Chrome'>, 'Chromium': <class 'webbrowser.Chrome'>, 'Elinks': <class 'webbrowser.Elinks'>, 'Error': <class 'webbrowser.Error'>, 'Galeon': <class 'webbrowser.Galeon'>, 'GenericBrowser': <class 'webbrowser.GenericBrowser'>, 'Grail': <class 'webbrowser.Grail'>, 'Konqueror': <class 'webbrowser.Konqueror'>, 'Mozilla': <class 'webbrowser.Mozilla'>, 'Netscape': <class 'webbrowser.Netscape'>, 'Opera': <class 'webbrowser.Opera'>, 'UnixBrowser': <class 'webbrowser.UnixBrowser'>, 'get': <function get at 0xb6543030>, 'main': <function main at 0xb641f150>, 'open': <function open at 0xb6543078>, 'open_new': <function open_new at 0xb6543420>, 'open_new_tab': <function open_new_tab at 0xb6543468>, 'os': <module 'os' from '/usr/lib/python3.7/os.py'>, 'register': <function register at 0xb655bcd8>, 'register_X_browsers': <function register_X_browsers at 0xb641ecd8>, 'register_standard_browsers': <function register_standard_browsers at 0xb641f108>, 'shlex': <module 'shlex' from '/usr/lib/python3.7/shlex.py'>, 'shutil': <module 'shutil' from '/usr/lib/python3.7/shutil.py'>, 'subprocess': <module 'subprocess' from '/usr/lib/python3.7/subprocess.py'>, 'sys': <module 'sys' (built-in)>, 'threading': <module 'threading' from '/usr/lib/python3.7/threading.py'>}
# >>> 
# >>> 
# >>> 1 and 2
# 2
# >>> 2 and 1
# 1
# >>> 
# >>> 
# >>> 
# >>> chain
# <62>:1: NameError: name 'chain' is not defined
# >>> globals()+itertools
# <auto.Importer.GWrap object at 0xb6441db0>
# >>> chain
# <class 'itertools.chain'>
# >>> 
# >>> 
# >>> dir(itertools)
# <59>:1: NameError: name 'itertools' is not defined
# >>> globals()+itertools
# <60>:1: NameError: name 'itertools' is not defined
# >>> chain
# <61>:1: NameError: name 'chain' is not defined
# >>> 
# >>> 
# >>> dict
# <class 'dict'>
# >>> pi
# 3.141592653589793
# >>> globals()+itertools-math
# <66>:1: NameError: name 'itertools' is not defined
# >>> pi
# 3.141592653589793
# >>> globals().get('pi')
# 3.141592653589793
# >>> 
# >>> 
# >>> 
# >>> 'x' in globals()
# False
# >>> 
# >>> 
# >>> autos()
# 'import http\nimport itertools\nimport math\nimport webbrowser\nimport xml\nimport xml.etree'
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
