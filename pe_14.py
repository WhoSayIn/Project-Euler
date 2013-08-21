#===============================================================================
# Project Euler - #14
# 
# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.
# 
# Hüseyin KELEŞ - admin@whosayin.com
# 7.7.2010
#===============================================================================

def bak(n, t, ilk):
    if n%2:
        snc = 3*n + 1
    else:
        snc = n/2
    if snc != 1:
        return bak(snc, t + 1, ilk)
    else:
        return t + 2, ilk

print(max(bak(i,0,i) for i in range(1,1000001)))

