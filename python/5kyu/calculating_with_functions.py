# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

def zero(arg=None): return 0 if not arg else arg(0)
def one(arg=None): return 1 if not arg else arg(1)
def two(arg=None): return 2 if not arg else arg(2)
def three(arg=None): return 3 if not arg else arg(3)
def four(arg=None): return 4 if not arg else arg(4)
def five(arg=None): return 5 if not arg else arg(5)
def six(arg=None): return 6 if not arg else arg(6)
def seven(arg=None): return 7 if not arg else arg(7)
def eight(arg=None): return 8 if not arg else arg(8)
def nine(arg=None): return 9 if not arg else arg(9)


def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda x: x*y
def divided_by(y): return lambda x: int(x/y)


print(seven(times(five())), 35)
