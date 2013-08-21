#===============================================================================
# Project Euler - #9
# 
# A Pythagorean triplet is a set of three natural numbers, a  < b  < c, for which,
# a^(2) + b^(2) = c^(2)
# 
# For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 
# Hüseyin KELEŞ - admin@whosayin.com - 2.7.2010
#===============================================================================

for a in range(1,999):
    for b in range(1,999):
        for c in range(999,1,-1):
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    print(a*b*c)
                    break