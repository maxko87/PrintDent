PrintDent
==========

Indents print statements based on how deep you are in the call stack. Useful for debugging.

Example:

```python
from printdent import pprint

def three():
    pprint("inside three")

def two():
    pprint("inside two")
    three()

def one():
    pprint("inside one")
    two()
    pprint("back inside one")

pprint("inside main")
one()
```

Output:

```
$ python example.py
inside main
  inside one
    inside two
      inside three
  back inside one
```
