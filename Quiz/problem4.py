from math import log


def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    val = 0
    while True:
        val += 1
        if 0 < x - b**val < b:
            return val


x = int(raw_input('x = '))
b = int(raw_input('b = '))
print myLog(x, b)
if log(x, b) == myLog(x, b):
    print "Success!"
