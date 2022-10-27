# Grammars

## Type Annotations

```py
def addTwo(x : Int) -> Int:
    return x + 2
```

## `if` Statement

```py
def type1(age):
    return 'adult' if age >= 18 else 'underage'

def type2(age):
    return age >= 18 and 'adult' or 'underage'

def type3(age):
    return ('underage', 'adult')[age >= 18]

def type4(age):
    return (lambda:'underage', lambda:'adult')[age >= 18]()

def type5(age):
    return {True:'adult', False:'underage'}[age >= 18]

def type6(age):
    return ((age >= 18) and ('adult',) or ('underage',))[0]
```

## List Comprehensions

```py
numbers = [1,2,3,4,5,6,7]
evens = [x for x in numbers if x % 2 is 0]
odds = [y for y in numbers if y not in evens]
```

## `dir()` Get Properties of the Arg

```py
>>> dir("Hello")
['__add__', '__class__', '__contains__', 
'__delattr__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', 
'__gt__', '__hash__', '__init__', 
'__init_subclass__', '__iter__', '__le__', 
'__len__', '__lt__', '__mod__', '__mul__', 
'__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__rmod__', 
'__rmul__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', 'capitalize', 
'casefold', 'center', 'count', 'encode', 'endswith', 
'expandtabs', 'find', 'format', 'format_map', 'index', 
'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 
'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
'istitle', 'isupper', 'join', 'ljust', 'lower', 
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
