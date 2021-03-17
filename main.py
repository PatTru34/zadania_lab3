#  Zadanie 1

# a = [ 1 -x for x in  range(1, 11, 1)]
# print(a)
#
# b = [ 4**y for y in range(8)]
# print(b)
#
# c = [x for x in b if x % 2 == 0]
# print(c)

# Zadanie 2
# from random import randint
# lista = [randint(0, 100) for x in range(10)]
# lista.sort()
# print(lista)
#
# listaparz = [x for x in lista if x%2==0]
# print(listaparz)

# Zadanie 3

# produkty = {"Banany":"kg", "Rodzynki":"paczka", "Arbuz":"szt","Mleko":"karton"}
# print(produkty)
#
# prod = [produkt for produkt in produkty.keys() if produkty[produkt] =="szt"]
# print(prod)

# Zadanie 4

# def czy_prostokatny(a, b, c):
#     big = None
#
#     if a > b and a > c:
#         big = a
#         a = c
#         c = big
#
#     if b > a and b > c:
#         big = b
#         b = c
#         c = big
#
#     return True if a ** 2 + b ** 2 == c ** 2 else False
#
# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))
#
# print(czy_prostokatny(a, b, c))

# Zadanie 5
# def pole_trapeza(a=0, b=0, h=0):
#     return ((a + b) * h)/2
#
# a = int(input("a:"))
# b = int(input("b:"))
# h = int(input("h:"))
# print(pole_trapeza(a, b, h))

# Zadanie 6

# a = int(input("a:"))
# b = int(input("b:"))
# ile = int(input("ile:"))
# def iloczyn_ciagu(a = 1, b = 4, ile = 10):
#     return a + (b * ile)
#
# print(iloczyn_ciagu(a,b,ile))

# Zadanie 7

# a = int(input("a:"))
# b = int(input("b:"))
# ile = int(input("ile:"))
# def te_same_dzialania(*args):
#     return args[0] + (args[1] * args[2])
#
# print(te_same_dzialania(a,b,ile))

# Zadanie 8

# def zakupy(**kwargs):
#     ile = len(kwargs.keys())
#     print(ile)
#     return sum(float(value) for value in kwargs.values())
#
# print(zakupy(jablka = 1, bagietka = 2, reklamyMastercard = "55", jakiskolejnyprodukt = 11.11))