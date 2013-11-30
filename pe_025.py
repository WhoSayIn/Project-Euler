#===============================================================================
# Project Euler - #25
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?
#
# Huseyin KELES - admin@whosayin.com
# 30.11.2013
#===============================================================================

def fibonacci(n):
    return _fib(n)[0]


# Returns a tuple (F(n), F(n+1))
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (2 * b - a)
        d = b * b + a * a
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

i = 1
while 1:
    if len(str(fibonacci(i))) == 1000:
        print i
        break
    i += 1
