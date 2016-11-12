Windows PowerShell
Copyright (C) 2013 Microsoft Corporation. All rights reserved.

PS C:\Users\NEW> python
Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
>>> help(str)
Help on class str in module __builtin__:

class str(basestring)
 |  str(object='') -> string
 |
 |  Return a nice string representation of the object.
 |  If the argument is a string, the return value is the same object.
 |
 |  Method resolution order:
 |      str
 |      basestring
 |      object
 |
 |  Methods defined here:
 |
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |
 |  __format__(...)
 |      S.__format__(format_spec) -> string
 |
 |      Return a formatted version of S as described by format_spec.
 |
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |
 |  __getnewargs__(...)
 |
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |
 |      Use of negative indices is not supported.
 |
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |
 |  __hash__(...)

>>>
>>>
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mo
d__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center',
 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'isl
ower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', '
rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate'
, 'upper', 'zfill']
>>>
>>>
>>>
>>> a = 5
>>> b = 6
>>>
>>>
>>> id(a)
41041192
>>>
>>>
>>> id(b)
41041180
>>>
>>>
>>>
>>> a = 5
>>> b = 5
>>>
>>> id(a)
41041192
>>> id(b)
41041192
>>>
>>>
>>> type(a)
<type 'int'>
>>>
>>>
>>> a is b
True
>>> a = 257
>>> b = 257
>>>
>>> a is b
False
>>> id(a)
43788152
>>> id(b)
41078108
>>> a = 128
>>> b = 128
>>> a is b
True
>>>
>>> a = 'abc'
>>> b = 'abc'
>>>
>>> id(a)
43041904
>>> id(b)
43041904
>>> a = 'abcdefgh'
>>> b = 'abcdefgh'
>>> a is b
True
>>> b = 'abcd efgh'
>>> a = 'abcd efgh'
>>>
>>>
>>> a is b
False
>>>
>>>
>>>
>>>
>>> a = 5
>>> b = 5
>>> a = 7
>>> b = 8
>>>
>>>
>>> a = 5.5
>>> type(a)
<type 'float'>
>>> a = 5
>>>
>>> type(a)
<type 'int'>
>>>
>>>
>>> a = 'hello'
>>> type(a)
<type 'str'>
>>>
>>>
>>> a
'hello'
>>> a = 5
>>> b = 6
>>> a,b = b,a
>>>
>>>
>>> a
6
>>> b
5
>>> a = 5
>>> b = 6
>>>
>>> a = 5.0 + 5
>>> type(a)
<type 'float'>
>>>
>>>
>>> 87378973897389738973893 * 12737171789217389173
1112961001296595206869485869318797467860489L
>>>
>>>
>>>
>>> s = 'hello everybody, hope you all are enjoying sat eveng'
>>>
>>> s[0] = 'h'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
>>>
>>> s = 'hello'
>>>
>>>
>>> s
'hello'
>>>
>>>
>>>
>>> s = 'hello everybody, hope you all are enjoying sat eveng'
>>>
>>>
>>> s[0]
'h'
>>> s[-1]
'g'
>>> s[-2]
'n'
>>> s[2]
'l'
>>> s[2:]
'llo everybody, hope you all are enjoying sat eveng'
>>>
>>> s[:5]
'hello'
>>>
>>>
>>> s[:4]
'hell'
>>> s[4:10]
'o ever'
>>>
>>>
>>> s[::-1]
'gneve tas gniyojne era lla uoy epoh ,ydobyreve olleh'
>>>
>>> s
'hello everybody, hope you all are enjoying sat eveng'
>>>
>>>
>>> s[::-2]
'geetsgion r l o ph,dbrv le'
>>>
>>>
>>>
>>> s
'hello everybody, hope you all are enjoying sat eveng'
>>>
>>>
>>>
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mo
d__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center',
 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'isl
ower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', '
rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate'
, 'upper', 'zfill']
>>>
>>>
>>>
>>> help(str)
Help on class str in module __builtin__:

class str(basestring)
 |  str(object='') -> string
 |
 |  Return a nice string representation of the object.
 |  If the argument is a string, the return value is the same object.
 |
 |  Method resolution order:
 |      str
 |      basestring
 |      object
 |
 |  Methods defined here:
 |
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |
 |  __format__(...)
 |      S.__format__(format_spec) -> string
 |
 |      Return a formatted version of S as described by format_spec.
 |
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |
 |  __getnewargs__(...)
 |
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |
 |      Use of negative indices is not supported.
 |
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |
 |  __mod__(...)
 |      x.__mod__(y) <==> x%y
 |
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |
 |  __rmod__(...)
 |      x.__rmod__(y) <==> y%x
 |
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |
 |  capitalize(...)
 |      S.capitalize() -> string
 |
 |      Return a copy of the string S with only its first character
 |      capitalized.
 |
 |  center(...)
 |      S.center(width[, fillchar]) -> string
 |
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int

>>>
>>>
>>>
>>> s
'hello everybody, hope you all are enjoying sat eveng'
>>>
>>>
>>> s.count(' ')
8
>>>
>>> s.count('y ')
0
>>> s.count(' y')
1
>>> s.count('fy')
0
>>> s.find(',')
15
>>>
>>> s.find('hj')
-1
>>>
>>> app = 'Hello, Mr {name}, Congrats You got {percent}% hike'
>>>
>>> app.format(percent=10, name='Awantik')
'Hello, Mr Awantik, Congrats You got 10% hike'
>>>
>>>
>>> app.format(percent=20, name='Awi')
'Hello, Mr Awi, Congrats You got 20% hike'
>>>
>>>
>>>
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mo
d__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center',
 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'isl
ower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', '
rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate'
, 'upper', 'zfill']
>>>
>>>
>>> s
'hello everybody, hope you all are enjoying sat eveng'
>>>
>>>
>>> url = 'www.google.com'
>>>
>>> url.endswith('com')
True
>>> url.startswith('www')
True
>>> url.startswith('wwww')
False
>>>
>>>
>>>
>>> s
'hello everybody, hope you all are enjoying sat eveng'
>>> s.index('hope')
17
>>> s.find('hope')
17
>>> s.index('hope4')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>>
>>>
>>>
>>> s.find('hope4')
-1
>>>
>>>
>>>
>>> s.find(' ')
5
>>> s.find(' ',6)
16
>>> s.find(' ',17)
21
>>> s = 'abc123'
>>>
>>> s.isalnum()
True
>>> s = 'abc 123'
>>>
>>>
>>> s.isalnum()
False
>>> s = 'abc'
>>>
>>> s.isalpha()
True
>>>
>>>
>>> s
'abc'
>>> s = '4234234'
>>>
>>>
>>> s.isdigit()
True
>>>
>>>
>>>
>>> s = '4234.234'
>>> s.isdigit()
False
>>>
>>>
>>>
>>>
>>> s
'4234.234'
>>> s = '    dssdsdsd   '
>>> s.lstrip()
'dssdsdsd   '
>>> s.rstrip()
'    dssdsdsd'
>>>
>>>
>>>
>>>
>>> s
'    dssdsdsd   '
>>> s.strip()
'dssdsdsd'
>>>
>>>
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mo
d__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center',
 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'isl
ower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', '
rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate'
, 'upper', 'zfill']
>>>
>>>
>>>
>>> s
'    dssdsdsd   '
>>> s = 'this is a great year isn't it'
  File "<stdin>", line 1
    s = 'this is a great year isn't it'
                                  ^
SyntaxError: invalid syntax
>>> s = "this is a great year isn't it"
>>>
>>>
>>> s
"this is a great year isn't it"
>>>
>>>
>>> s.replace(' ','*')
"this*is*a*great*year*isn't*it"
>>>
>>>
>>>
>>> s.replace('is','hello')
"thhello hello a great year hellon't it"
>>>
>>>
>>> s
"this is a great year isn't it"
>>> s = 'This is Great'
>>> s.swapcase()
'tHIS IS gREAT'
>>>
>>>
>>> s = '213213.767'
>>> s.partition()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: partition() takes exactly one argument (0 given)
>>> s.partition('.')
('213213', '.', '767')
>>>
>>>
>>>
>>> s.partition('.')
('213213', '.', '767')
>>> f,s,l = s.partition('.')
>>>
>>> f.isdigit()
True
>>> f.isdigit() and l.isdigit() and s == '.'
True
>>>
>>>
>>>
>>>
>>> s = '213213.76.7'
>>> f.isdigit() and l.isdigit() and s == '.'
False
>>> s = '213213767'
>>>
>>> f.isdigit() and l.isdigit() and s == '.'
False
>>> s
'213213767'
>>> s = '213213767'
>>>
>>>
>>> f,se,l = s.partition('.')
>>>
>>> se
''
>>>
>>>
>>>
>>> s
'213213767'
>>>
>>>
>>>
>>> l = []
>>> l = list()
>>>
>>>
>>> l.append(1)
>>> l.append('hello')
>>> l
[1, 'hello']
>>>
>>>
>>> l[2] = 'great'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> l.append('how')
>>>
>>>
>>> l
[1, 'hello', 'how']
>>> len(l)
3
>>>
>>>
>>>
>>> l = [2,3,54,6,67]
>>>
>>> l
[2, 3, 54, 6, 67]
>>>
>>>
>>>
>>> sum(l)
132
>>>
>>> max(l)
67
>>>
>>> min(l)
2
>>>
>>>
>>>
>>> l[0] = 'great'
>>>
>>>
>>> l
['great', 3, 54, 6, 67]
>>>
>>>
>>>
>>>
>>>
>>>
>>> l
['great', 3, 54, 6, 67]
>>>
>>> l[2] = [5,7,7,5]
>>> l
['great', 3, [5, 7, 7, 5], 6, 67]
>>> l[2]
[5, 7, 7, 5]
>>> l[2][1]
7
>>>
>>> l = [ [1,2,3], [4,5,6], [7,8,9] ]
>>>
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> l[1][1]
5
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>>
>>>
>>> m = [ 9,9,9 ]
>>>
>>> l.append(m)
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9]]
>>>
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9]]
>>>
>>>
>>>
>>>
>>> type(l) == list
True
>>>
>>> isinstance(list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: isinstance expected 2 arguments, got 1
>>> isinstance(l, list)
True
>>>
>>>
>>>
>>>
>>>
>>> m
[9, 9, 9]
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9]]
>>>
>>>
>>> l.extend(m)
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9], 9, 9, 9]
>>>
>>>
>>>
>>>
>>> a = [1,2,3]
>>> b = [7,8,9]
>>> a.extend(b)
>>>
>>> a
[1, 2, 3, 7, 8, 9]
>>>
>>>
>>> a
[1, 2, 3, 7, 8, 9]
>>>
>>>
>>> a = [1,2,3]
>>>
>>>
>>> b
[7, 8, 9]
>>> a.append(b)
>>>
>>>
>>> a
[1, 2, 3, [7, 8, 9]]
>>>
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__'
, '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
 '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '
__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'a
ppend', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>>
>>>
>>> a
[1, 2, 3, [7, 8, 9]]
>>>
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9], 9, 9, 9]
>>>
>>>
>>> l.count(9)
3
>>>
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9], 9, 9, 9]
>>> s = 'abcdef'
>>> l.extend(s)
>>>
>>>
>>>
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9], 9, 9, 9, 'a', 'b', 'c', 'd', 'e', 'f']
>>>
>>>
>>>
>>> l.index(9)
4
>>> l.index(9,5)
5
>>> l.insert(4,'hello')
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9], 'hello', 9, 9, 9, 'a', 'b', 'c', 'd', 'e', 'f']
>>>
>>>
>>>
>>> l.extend([5,6,6,[7,7,7]])
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9], 'hello', 9, 9, 9, 'a', 'b', 'c', 'd', 'e', 'f', 5, 6, 6, [7, 7, 7]]
>>>
>>>
>>>
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9], 'hello', 9, 9, 9, 'a', 'b', 'c', 'd', 'e', 'f', 5, 6, 6, [7, 7, 7]]
>>>
>>>
>>>
>>> l.pop(5)
9
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9], 'hello', 9, 9, 'a', 'b', 'c', 'd', 'e', 'f', 5, 6, 6, [7, 7, 7]]
>>> l.remove('hello')
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9], 9, 9, 'a', 'b', 'c', 'd', 'e', 'f', 5, 6, 6, [7, 7, 7]]
>>>
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9], 9, 9, 'a', 'b', 'c', 'd', 'e', 'f', 5, 6, 6, [7, 7, 7]]
>>> l.reverse()
>>> l
[[7, 7, 7], 6, 6, 5, 'f', 'e', 'd', 'c', 'b', 'a', 9, 9, [9, 9, 9], [7, 8, 9], [4, 5, 6], [1, 2, 3]]
>>>
>>>
>>>
>>> l.reverse()
>>>
>>> l
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9], 9, 9, 'a', 'b', 'c', 'd', 'e', 'f', 5, 6, 6, [7, 7, 7]]
>>>
>>>
>>> a = ['zeb','abc','cat']
>>>
>>> a.sort()
>>>
>>> a
['abc', 'cat', 'zeb']
>>> a.sort(reverse=true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> a.sort(reverse=True)
>>>
>>> a
['zeb', 'cat', 'abc']
>>>
>>>
>>> s
'abcdef'
>>> s = 'hello world, here I come again to bother you all'
>>>
>>> s.split()
['hello', 'world,', 'here', 'I', 'come', 'again', 'to', 'bother', 'you', 'all']
>>>
>>>
>>> l = s.split()
>>> l
['hello', 'world,', 'here', 'I', 'come', 'again', 'to', 'bother', 'you', 'all']
>>> l.sort()
>>>
>>> l
['I', 'again', 'all', 'bother', 'come', 'hello', 'here', 'to', 'world,', 'you']
>>> ' '.join(l)
'I again all bother come hello here to world, you'
>>>
>>>
>>> s = 'hellosdasalsalsuahs'
>>> s.split('a')
['hellosd', 's', 'ls', 'lsu', 'hs']
>>> x = s.split('a')
>>> '*'.join(x)
'hellosd*s*ls*lsu*hs'
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> db = {}
>>>
>>> db = dict()
>>>
>>> db['awantik'] = 30
>>> db['abhi'] = 25
>>> db['jack'] = 24
>>>
>>> db
{'awantik': 30, 'abhi': 25, 'jack': 24}
>>>
>>>
>>> db['jack']
24
>>>
>>>
>>>
>>> db.items()
[('awantik', 30), ('abhi', 25), ('jack', 24)]
>>>
>>>
>>>
>>>
>>> db.values()
[30, 25, 24]
>>> db.keys()
['awantik', 'abhi', 'jack']
>>>
>>>
>>>
>>> db['awantik'] = [1,2,3,4]
>>>
>>> db
{'awantik': [1, 2, 3, 4], 'abhi': 25, 'jack': 24}
>>> db['awantik']
[1, 2, 3, 4]
>>>
>>> db['awantik'].append(777)
>>>
>>> db
{'awantik': [1, 2, 3, 4, 777], 'abhi': 25, 'jack': 24}
>>> db['abhi'] = {'a':100, 'b':200}
>>>
>>> db
{'awantik': [1, 2, 3, 4, 777], 'abhi': {'a': 100, 'b': 200}, 'jack': 24}
>>> db['abhi']
{'a': 100, 'b': 200}
>>> db['abhi']['c'] = 700
>>>
>>> db
{'awantik': [1, 2, 3, 4, 777], 'abhi': {'a': 100, 'c': 700, 'b': 200}, 'jack': 24}
>>>
>>>
>>>
>>>
>>> dir(set)
['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getat
tribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__le
n__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub
__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy
', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issup
erset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>>
>>>
>>>
>>> s = set([2,5,2,1,1,6])
>>> s
set([1, 2, 5, 6])
>>>
>>>
>>>
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mo
d__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center',
 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'isl
ower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', '
rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate'
, 'upper', 'zfill']
>>>
>>>
>>>
>>> s
set([1, 2, 5, 6])
>>>
>>>
>>> s2 = set(4,5,6,7,2])
  File "<stdin>", line 1
    s2 = set(4,5,6,7,2])
                      ^
SyntaxError: invalid syntax
>>> s2 = set(4,5,6,7,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set expected at most 1 arguments, got 5
>>> s2 = set([4,5,6,7,2])
>>>
>>>
>>>
>>> s
set([1, 2, 5, 6])
>>> s2
set([2, 4, 5, 6, 7])
>>> s + s2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s | s2
set([1, 2, 4, 5, 6, 7])
>>>
>>> s ^ s2
set([1, 4, 7])
>>> s & s2
set([2, 5, 6])
>>>
>>>
>>>
>>> s & s2
set([2, 5, 6])
>>>
>>> s - s2
set([1])
>>>
>>>
>>> s2 - s
set([4, 7])
>>>
>>>
>>>
>>> s
set([1, 2, 5, 6])
>>>
>>> s2
set([2, 4, 5, 6, 7])
>>>
>>>
>>>
>>>
>>> s ^ s2
set([1, 4, 7])
>>>
>>>
>>>
>>>
>>>
>>> help(set)
Help on class set in module __builtin__:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |
 |  Build an unordered collection of unique elements.
 |
 |  Methods defined here:
 |
 |  __and__(...)
 |      x.__and__(y) <==> x&y
 |
 |  __cmp__(...)
 |      x.__cmp__(y) <==> cmp(x,y)
 |
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |
 |  __iand__(...)
 |      x.__iand__(y) <==> x&=y
 |
 |  __init__(...)
 |      x.__init__(...) initializes x; see help(type(x)) for signature
 |
 |  __ior__(...)
 |      x.__ior__(y) <==> x|=y
 |
 |  __isub__(...)
 |      x.__isub__(y) <==> x-=y
 |
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |
 |  __ixor__(...)
 |      x.__ixor__(y) <==> x^=y
 |
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |
 |  __or__(...)
 |      x.__or__(y) <==> x|y
 |
 |  __rand__(...)
 |      x.__rand__(y) <==> y&x
 |
 |  __reduce__(...)
 |      Return state information for pickling.
 |
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |
 |  __ror__(...)
 |      x.__ror__(y) <==> y|x
 |
 |  __rsub__(...)
 |      x.__rsub__(y) <==> y-x
 |
 |  __rxor__(...)
 |      x.__rxor__(y) <==> y^x
 |
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |
 |  __sub__(...)
 |      x.__sub__(y) <==> x-y
 |
 |  __xor__(...)
 |      x.__xor__(y) <==> x^y
 |
 |  add(...)
 |      Add an element to a set.
 |
 |      This has no effect if the element is already present.
 |
 |  clear(...)
 |      Remove all elements from this set.
 |
 |  copy(...)
 |      Return a shallow copy of a set.
 |
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |
 |      (i.e. all elements that are in this set but not the others.)
 |
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |
 |      If the element is not a member, do nothing.
 |
 |  intersection(...)
 |      Return the intersection of two or more sets as a new set.
 |
 |      (i.e. elements that are common to all of the sets.)
 |
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |
 |  issubset(...)
 |      Report whether another set contains this set.
 |
 |  issuperset(...)
 |      Report whether this set contains another set.
 |
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |
 |      If the element is not a member, raise a KeyError.
 |
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |
 |      (i.e. all elements that are in exactly one of the sets.)
 |
 |  symmetric_difference_update(...)

>>> dir(set)
['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getat
tribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__le
n__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub
__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy
', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issup
erset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>>
>>>
>>>
>>> s
set([1, 2, 5, 6])
>>> s.add(61)
>>> s
set([1, 2, 5, 6, 61])
>>> s2
set([2, 4, 5, 6, 7])
>>>
>>>
>>>
>>>
>>>
>>> s.union(s2)
set([1, 2, 4, 5, 6, 7, 61])
>>> s
set([1, 2, 5, 6, 61])
>>>
>>> s | s2
set([1, 2, 4, 5, 6, 7, 61])
>>>
>>>
>>>
>>> import collections
>>>
>>>
>>> dir(collections)
['Callable', 'Container', 'Counter', 'Hashable', 'ItemsView', 'Iterable', 'Iterator', 'KeysView', 'Mapping', 'MappingVie
w', 'MutableMapping', 'MutableSequence', 'MutableSet', 'OrderedDict', 'Sequence', 'Set', 'Sized', 'ValuesView', '__all__
', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_abcoll', '_chain', '_class_template', '_eq', '_fi
eld_template', '_get_ident', '_heapq', '_imap', '_iskeyword', '_itemgetter', '_repeat', '_repr_template', '_starmap', '_
sys', 'defaultdict', 'deque', 'namedtuple']
>>> help(collections)
Help on module collections:

NAME
    collections

FILE
    c:\python27\lib\collections.py

DESCRIPTION
    This module implements specialized container datatypes providing
    alternatives to Python's general purpose built-in containers, dict,
    list, set, and tuple.

    * namedtuple   factory function for creating tuple subclasses with named fields
    * deque        list-like container with fast appends and pops on either end
    * Counter      dict subclass for counting hashable objects
    * OrderedDict  dict subclass that remembers the order entries were added
    * defaultdict  dict subclass that calls a factory function to supply missing values

CLASSES
    __builtin__.dict(__builtin__.object)
        Counter
        OrderedDict
        defaultdict
    __builtin__.object
        _abcoll.Callable
        _abcoll.Container
        _abcoll.Hashable
        _abcoll.Iterable
            _abcoll.Iterator
        _abcoll.Sized
            _abcoll.Mapping(_abcoll.Sized, _abcoll.Iterable, _abcoll.Container)
                _abcoll.MutableMapping
            _abcoll.MappingView
                _abcoll.ItemsView(_abcoll.MappingView, _abcoll.Set)
                _abcoll.KeysView(_abcoll.MappingView, _abcoll.Set)
                _abcoll.ValuesView
            _abcoll.Sequence(_abcoll.Sized, _abcoll.Iterable, _abcoll.Container)
                _abcoll.MutableSequence
            _abcoll.Set(_abcoll.Sized, _abcoll.Iterable, _abcoll.Container)
                _abcoll.MutableSet
        deque

    class Callable(__builtin__.object)
     |  Methods defined here:
     |
     |  __call__(self, *args, **kwds)
     |
     |  ----------------------------------------------------------------------

>>>
>>>
>>>
>>>
>>>
>>> cnt = Counter()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Counter' is not defined
>>> import collections.Counter
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named Counter
>>>
>>>
>>>
>>> import collections
>>>
>>> help(Counter)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Counter' is not defined
>>> help(collections)
Help on module collections:

NAME
    collections

FILE
    c:\python27\lib\collections.py

DESCRIPTION
    This module implements specialized container datatypes providing
    alternatives to Python's general purpose built-in containers, dict,
    list, set, and tuple.

    * namedtuple   factory function for creating tuple subclasses with named fields
    * deque        list-like container with fast appends and pops on either end
    * Counter      dict subclass for counting hashable objects
    * OrderedDict  dict subclass that remembers the order entries were added
    * defaultdict  dict subclass that calls a factory function to supply missing values

CLASSES
    __builtin__.dict(__builtin__.object)
        Counter
        OrderedDict
        defaultdict
    __builtin__.object
        _abcoll.Callable
        _abcoll.Container
        _abcoll.Hashable
        _abcoll.Iterable
            _abcoll.Iterator
        _abcoll.Sized
            _abcoll.Mapping(_abcoll.Sized, _abcoll.Iterable, _abcoll.Container)
                _abcoll.MutableMapping
            _abcoll.MappingView
                _abcoll.ItemsView(_abcoll.MappingView, _abcoll.Set)
                _abcoll.KeysView(_abcoll.MappingView, _abcoll.Set)
                _abcoll.ValuesView
            _abcoll.Sequence(_abcoll.Sized, _abcoll.Iterable, _abcoll.Container)
                _abcoll.MutableSequence
            _abcoll.Set(_abcoll.Sized, _abcoll.Iterable, _abcoll.Container)
                _abcoll.MutableSet
        deque

    class Callable(__builtin__.object)
     |  Methods defined here:
     |
     |  __call__(self, *args, **kwds)
     |
     |  ----------------------------------------------------------------------

>>>
>>>
>>> import collections
>>>
>>> cnt = collections.Counter()
>>>
>>> l = ['red','blue','red','green','blue','yellow']
>>>
>>> for w in l:
...    cnt[w] += 1
...
>>> cnt
Counter({'blue': 2, 'red': 2, 'green': 1, 'yellow': 1})
>>>
>>>
>>> cnt
Counter({'blue': 2, 'red': 2, 'green': 1, 'yellow': 1})
>>> cnt = collections.Counter()
>>>
>>> cnt
Counter()
>>> cnt('asbabsjahsjas').most_common(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Counter' object is not callable
>>>
>>> collections.Counter('asbabsjahsjas').most_common(2)
[('a', 4), ('s', 4)]
>>>
>>> help(cnt)
Help on Counter in module collections object:

class Counter(__builtin__.dict)
 |  Dict subclass for counting hashable items.  Sometimes called a bag
 |  or multiset.  Elements are stored as dictionary keys and their counts
 |  are stored as dictionary values.
 |
 |  >>> c = Counter('abcdeabcdabcaba')  # count elements from a string
 |
 |  >>> c.most_common(3)                # three most common elements
 |  [('a', 5), ('b', 4), ('c', 3)]
 |  >>> sorted(c)                       # list all unique elements
 |  ['a', 'b', 'c', 'd', 'e']
 |  >>> ''.join(sorted(c.elements()))   # list elements with repetitions
 |  'aaaaabbbbcccdde'
 |  >>> sum(c.values())                 # total of all counts
 |  15
 |
 |  >>> c['a']                          # count of letter 'a'
 |  5
 |  >>> for elem in 'shazam':           # update counts from an iterable
 |  ...     c[elem] += 1                # by adding 1 to each element's count
 |  >>> c['a']                          # now there are seven 'a'
 |  7
 |  >>> del c['b']                      # remove all 'b'
 |  >>> c['b']                          # now there are zero 'b'
 |  0
 |
 |  >>> d = Counter('simsalabim')       # make another counter
 |  >>> c.update(d)                     # add in the second counter
 |  >>> c['a']                          # now there are nine 'a'
 |  9
 |
 |  >>> c.clear()                       # empty the counter
 |  >>> c
 |  Counter()
 |
 |  Note:  If a count is set to zero or reduced to zero, it will remain
 |  in the counter until the entry is deleted or the counter is cleared:
 |
 |  >>> c = Counter('aaabbc')
 |  >>> c['b'] -= 2                     # reduce the count of 'b' by two
 |  >>> c.most_common()                 # 'b' is still in, but its count is zero
 |  [('a', 3), ('c', 1), ('b', 0)]
 |
 |  Method resolution order:
 |      Counter
 |      __builtin__.dict
 |      __builtin__.object
 |
 |  Methods defined here:
 |
 |  __add__(self, other)
 |      Add counts from two counters.
 |
 |      >>> Counter('abbb') + Counter('bcc')
 |      Counter({'b': 4, 'c': 2, 'a': 1})
 |
 |  __and__(self, other)
 |      Intersection is the minimum of corresponding counts.
 |
 |      >>> Counter('abbb') & Counter('bcc')
 |      Counter({'b': 1})
 |
 |  __delitem__(self, elem)
 |      Like dict.__delitem__() but does not raise KeyError for missing values.
 |
 |  __init__(*args, **kwds)
 |      Create a new, empty Counter object.  And if given, count elements
 |      from an input iterable.  Or, initialize the count from another mapping
 |      of elements to their counts.
 |
 |      >>> c = Counter()                           # a new, empty counter
 |      >>> c = Counter('gallahad')                 # a new counter from an iterable
 |      >>> c = Counter({'a': 4, 'b': 2})           # a new counter from a mapping
 |      >>> c = Counter(a=4, b=2)                   # a new counter from keyword args
 |
 |  __missing__(self, key)
 |      The count of elements not in the Counter is zero.
 |
 |  __or__(self, other)
 |      Union is the maximum of value in either of the input counters.
 |
 |      >>> Counter('abbb') | Counter('bcc')
 |      Counter({'b': 3, 'c': 2, 'a': 1})
 |
 |  __reduce__(self)
 |
 |  __repr__(self)
 |
 |  __sub__(self, other)
 |      Subtract count, but keep only results with positive counts.
 |
 |      >>> Counter('abbbc') - Counter('bccd')
 |      Counter({'b': 2, 'a': 1})
 |
 |  copy(self)
 |      Return a shallow copy.
 |
 |  elements(self)
 |      Iterator over elements repeating each as many times as its count.
 |
 |      >>> c = Counter('ABCABC')
 |      >>> sorted(c.elements())
 |      ['A', 'A', 'B', 'B', 'C', 'C']
 |
 |      # Knuth's example for prime factors of 1836:  2**2 * 3**3 * 17**1
 |      >>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
 |      >>> product = 1
 |      >>> for factor in prime_factors.elements():     # loop over factors
 |      ...     product *= factor                       # and multiply them
 |      >>> product
 |      1836
 |
 |      Note, if an element's count has been set to zero or is a negative
 |      number, elements() will ignore it.
 |
 |  most_common(self, n=None)
 |      List the n most common elements and their counts from the most
 |      common to the least.  If n is None, then list all element counts.
 |
 |      >>> Counter('abcdeabcdabcaba').most_common(3)
 |      [('a', 5), ('b', 4), ('c', 3)]
 |
 |  subtract(*args, **kwds)
 |      Like dict.update() but subtracts counts instead of replacing them.
 |      Counts can be reduced below zero.  Both the inputs and outputs are
 |      allowed to contain zero and negative counts.
 |
 |      Source can be an iterable, a dictionary, or another Counter instance.
 |
 |      >>> c = Counter('which')
 |      >>> c.subtract('witch')             # subtract elements from another iterable
 |      >>> c.subtract(Counter('watch'))    # subtract elements from another counter
 |      >>> c['h']                          # 2 in which, minus 1 in witch, minus 1 in watch
 |      0
 |      >>> c['w']                          # 1 in which, minus 1 in witch, minus 1 in watch
 |      -1
 |
 |  update(*args, **kwds)
 |      Like dict.update() but add counts instead of replacing them.
 |
 |      Source can be an iterable, a dictionary, or another Counter instance.
 |
 |      >>> c = Counter('which')
 |      >>> c.update('witch')           # add elements from another iterable
 |      >>> d = Counter('watch')
 |      >>> c.update(d)                 # add elements from another counter
 |      >>> c['h']                      # four 'h' in which, witch, and watch
 |      4
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  fromkeys(cls, iterable, v=None) from __builtin__.type
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from __builtin__.dict:
 |
 |  __cmp__(...)
 |      x.__cmp__(y) <==> cmp(x,y)
 |
 |  __contains__(...)
 |      D.__contains__(k) -> True if D has a key k, else False
 |
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |
 |  __setitem__(...)
 |      x.__setitem__(i, y) <==> x[i]=y
 |
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |
 |  has_key(...)
 |      D.has_key(k) -> True if D has a key k, else False
 |
 |  items(...)
 |      D.items() -> list of D's (key, value) pairs, as 2-tuples
 |
 |  iteritems(...)
 |      D.iteritems() -> an iterator over the (key, value) items of D
 |
 |  iterkeys(...)
 |      D.iterkeys() -> an iterator over the keys of D
 |
 |  itervalues(...)
 |      D.itervalues() -> an iterator over the values of D
 |
 |  keys(...)
 |      D.keys() -> list of D's keys
 |
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |

>>>
>>>
>>>
>>> d = {'mango':10, 'banana':20, 'apple':15}
>>>
>>>
>>> d
{'mango': 10, 'banana': 20, 'apple': 15}
>>> d = {'zebra':44, 'mango':10, 'banana':20, 'apple':15}
>>> d
{'mango': 10, 'apple': 15, 'zebra': 44, 'banana': 20}
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> l
['red', 'blue', 'red', 'green', 'blue', 'yellow']
>>>
>>>
>>> l = [ ['awi',45], ['bat',4] ,['crow',67] ]
>>>
>>> def getKey(x):
...   return x[1]
...
>>> sorted(l, key=getKey)
[['bat', 4], ['awi', 45], ['crow', 67]]
>>>
>>>
>>>
>>>
>>>
>>> l = lambda x : x + 2
>>> l(4)
6
>>> type(l)
<type 'function'>
>>>
