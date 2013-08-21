#===============================================================================
# Project Euler - #20
# 
# n! means n × (n  − 1) × ... × 3 × 2 × 1
# 
# Find the sum of the digits in the number 100!
# 
# Hüseyin KELEŞ - admin@whosayin.com 2.7.2010
#===============================================================================

from math import factorial

sum = 0
for i in str(factorial(100)):
    sum += int(i)
print(sum)