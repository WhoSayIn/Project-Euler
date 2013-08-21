#===============================================================================
# Project Euler - #52
# Hüseyin KELEŞ - admin@whosayin.com
# 27.06.2010
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# 
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
#===============================================================================
i = 0
while 1:
    i += 1
    if sorted(str(i)) == sorted(str(i*2)) == sorted(str(i*3)) == sorted(str(i*4)) == sorted(str(i*5)) == sorted(str(i*6)):
        print("Doğru Cevap =", i)
        break