from math import sqrt

# zadnie 7
a = int(input("Podaj liczbe"))
try:
    sqrt(a)
except ValueError:
    print("Bład wartość jest ujemna")
