# zadanie 1

A = [1 - x for x in range(1, 11)]
B = [4 ** i for i in range(7)]
C = [x for x in B if x % 2 == 0]

# zadanie 2
lista = [1, 4, 5, 6, 7, 8, 9, 1, 2, 0]
list2 = [i for i in lista if i % 2 == 0]

# zadanie 3
produkty = {'mleko': 'l', 'jajka': 'sztuki', 'maka': 'kg', 'sol': 'kg', 'woda': 'l'}
produktySztuki = {k: v for k, v in produkty.items() if v == 'sztuki'}
print(produktySztuki)


# zadnie 4
def czyTrojkatProstokatny(a, b, c):
    return c ** 2 == (a ** 2) + (b ** 2)


# zadanie 5
def poleTrapezu(a=1, b=1, h=1):
    return ((a + b) * h) / 2


# zadanie 6
def iloczynCiagu(a=1, b=4, ile=10):
    iloczyn = a
    for i in range(ile):
        iloczyn *= b
    return iloczyn


print(iloczynCiagu())
