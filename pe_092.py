#===============================================================================
# Project Euler - #25
#
# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
#
# For example,
#
# 44  32  13  10  1  1
# 85  89  145  42  20  4  16  37  58  89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?
#
# Huseyin KELES - admin@whosayin.com
# 30.11.2013
#===============================================================================

# TODO cache the values that returns true, so next time we dont have to recalculate

def endsWith89(n):
    if n == 1 :
        return 0
    if n == 89:
        return 1

    return endsWith89(sum([int(i) ** 2 for i in str(n)]))

print sum([endsWith89(i) for i in range (1, 10000000)])
