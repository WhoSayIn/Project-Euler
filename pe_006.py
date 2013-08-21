#===============================================================================
# Project Euler - #6
# Hüseyin KELEŞ - admin@whosayin.com
# 27.06.2010
# The sum of the squares of the first ten natural numbers is,
# 1^(2) + 2^(2) + ... + 10^(2) = 385
# 
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^(2) = 55^(2) = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#===============================================================================
hedef = 101

ktoplam = toplamk = 0

for i in range(hedef):
    ktoplam += i**2
    toplamk += i
    
toplamk = toplamk**2

print("Kareleri toplamı =", ktoplam)

print("Toplamlarının karesi =", toplamk)

sonuc = toplamk - ktoplam
print("Sonuç =", sonuc)
