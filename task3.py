# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import random

a = random.randint (1, 1000)

b = 2

c = None

i = 1

while b**i < a:
    i += 1
    c = b**i
    print(" ")
    print(c)
    if c > a/2:
        break
print(a)


