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