def asal (n):
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


asallar = 2

for i in range(3,2000000,2):
    if asal(i):
        asallar += i
print(asallar)