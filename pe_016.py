#===============================================================================
# Project Euler - #16
# 2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^(1000)?
# Hüseyin KELEŞ - admin@whosayin.com - 2.7.2010
#===============================================================================


a=0
for i in str(2**1000):
    a+=int(i)
print(a)