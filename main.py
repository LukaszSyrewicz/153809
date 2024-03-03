# a = 56
# print(a)
# print(type(a))
# b = 5.5
# print(b)
# print(type(b))
# zmienna_tekstowa = 'wizualizacja danych'
# print(zmienna_tekstowa)
# print(type(zmienna_tekstowa))
import sys

# a = 6
# b = 3.55
# c = a + b
# print(c)
# d = a - b
# print(d)
# e = 4
# f = b // a
# print(f)
# f = a // b
# print(f)
# g = a ** 2
# print(g)
# h = pow(a,2)
# print(h)
# ##
# i = 6 ** (1/2)
# j = pow(6,1/2)
# print(i)
# print(j)
#
# k = 'wizualizacja danych'
# l = ' grupa '
# m = 1
# print(k + l + str(m))
# print('Liczba a jeste równa {: .2f}, liczba b jest równa {:f}'.format(a, b))
# print('Liczba a jeste równa {:f}, liczba b jest równa {}'.format(a, b))
#########################################################
# a = input('Wprowadz liczbe: ')
# print(a)
# print(type(a))
#
# print(a * 5)
# print(type(a))
# sys.stdout.write('Wprowadz liczbe: ')
# b = sys.stdin.readline()
# print(b)
# print(type(b))
# print(b + ' To wartosci liczby b')
# print(type(b))
######################################################
#lista = [5, 6.6, 34, 'a', 'b', [2, 3, 4], 'ab']
# print(lista)
# lista.append(67)
# print(lista)
# lista.extend([20, 21, 22])
# print(lista)
# lista.pop()
# print(lista)
# lista.pop(2)
# print(lista)
# lista.remove([2, 3, 4])
# print(lista)
# del lista[1]
# print(lista)
# # del lista
# print(lista)
# lista.reverse()
# print(lista)
# lista.sort()
# print(lista)
#######################################
# slownik = {'klucz': 'wartosc', 1 : 2,'a': 5, 4: 'b'}
# print(slownik)
# print(slownik[4])
# slownik[6] = 45
# print(slownik)
# slownik.pop(1)
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# del slownik[6]
########################################
# a = 8
# b = 8
# if a > b:
#     print('a jest wieksze od b')
# elif a < b:
#     print('b jest wieksze od a')
# else:
#     print('a jest rowne b')
########################################
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if (a > b) & (c > d):
#     print(a, c)
# else:
#     print(b, d)
#
# for i in range(0, 8, 2):
#     print(i)
# else:
#     print('koniec petli')

# for i in lista:
#     print(i)

# for i in range(0, 5):
#     for j in range(0,5):
#         result = i + j
#         print(result)
#     print('')

# licznik = 0
# while licznik < len(lista):
#     print(lista[licznik])
#     licznik += 1
# else:
#     print('koniec petli')

# licznik = 0
# while licznik != 10:
#     if licznik == 7:
#         print(licznik)
#         break;
#     else:
#         licznik+=1
# else:
#     print('licznik')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sys.stdout.write('podaj liczbe: ')
a = sys.stdin.readline()
print(a)
i = 0
while i < len(lista):
    if a - lista[i] == 0:
        print(i, lista[i])
        break
    else:
        i+=1
else:
    print('nie ma takiej liczby')


if a in lista:
    print(a)
else:
    print('nie ma tkaiej liczby')