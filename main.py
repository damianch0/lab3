from math import *


# # try except
# try:
#     a = int(input())
#     b = int(input())
#
#     result = a / b
# # except ZeroDivisionError:
# #     print("nie mozna dzielic przez zerooo")
# # except ValueError:
# #     print("Nie poprawana liczba")
# except Exception:
#     print("Inny bład")
# else:
#     print(result)

# pyton comprehension

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = []
# print(l1)
# for i in l1:
#     l2.append(i ** 2)
# print(l2)
#
# l2 = [i ** 2 for i in l1]
# print(l2)
#
# l3 = [3 ** y for y in range(1, 6)]
# print(l3)
#
# l4 = [ x for x in l1 if x % 2 != 0]
# print(l4)
#
# l5 = [(x, y) for x in l2 for y in l3]
# print(l5)

#
# s1 = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9}
# s2 = {}
# for key, val in s1.items():
#     s2[val] = key
# print(s1)
# print(s2)
#
# s3 = {v: k for k, v in s1.items()}
# print(s3)


# funkcje
#
# def rownanie_kwadratowe(a, b, c):
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print('Brak pierwiastow')
#         return 0
#     elif delta == 0:
#         print('Jeden pierwiaste')
#         x = (-b / (2 * a))
#         return x
#     else:
#         print('dwa pierwiastki')
#         x1 = ((-b - sqrt(delta)) / (2 * a))
#         x2 = ((-b + sqrt(delta)) / (2 * a))
#         return x1, x2
#
# print(rownanie_kwadratowe(6, 3, 1))
# print(rownanie_kwadratowe(1, 2, 1))
# print(rownanie_kwadratowe(2, 6, 1))
#
#
# def dlugos_odcinka(x1=1, x2=2, y1=3, y2=4):
#     return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#
#
# print(dlugos_odcinka())
# print(3, 5, 1, 6)
# print(dlugos_odcinka(y1=5, x1=3, y2=6, x2=8))
# print(dlugos_odcinka(1, 5, y2=8, y1=3))
#
#

#
# plik = open('D:\\129781\\lab3\\tekst.txt', 'r', encoding = 'utf-8')
# znak = plik.read(10)
# linia = plik.readline()
# linie = plik.readlines()
# plik.close()
# print(znak)
# print(linia)
# print(linie)

# plik = open('tekst.txt', 'a+')
# plik.write('aaaaa')
# plik.seek(105)
# znaki = plik.read(10)
# print(znaki)
# plik.close()

with open('tekst.txt', 'r') as plik:
    znaki = plik.read(10)

print(znaki)