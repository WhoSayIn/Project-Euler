#===============================================================================
# Project Euler - #1
# 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.
# 
# Hüseyin KELEŞ - admin@whosayin.com
# 6.7.2010
# 1 milyon için ilk 0.610776901245 --- 233333166668
# 1 milyon için iki 0.001986980438 --- 233333166668
#===============================================================================
from math import floor

def bln(n):
    p = floor(999 / n)
    return n * (p * (p + 1)) / 2

toplam = bln(3) + bln(5) - bln(15)
print(int(toplam))