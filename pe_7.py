def asal (n):
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


asallar = 1
sayac   = 2
while asallar != 10001:
    sayac+=1
    if asal(sayac):
        asallar+=1
print(sayac)