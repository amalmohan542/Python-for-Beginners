# Python Program to Print triangle Pattern
'''
*

* *

* * *

'''


def stars(n):
    for i in range(0, n + 1):
        for j in range(0, i):
            print("* ", end='')
        print("\n")


n = int(input("Enter a number : "))
stars(n)
