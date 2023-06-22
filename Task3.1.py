import random

a = random.randint (1, 700)

b = 2

i = 0
while b ** i <= a:
    print(b ** i)
    print(" ")
    i +=1
print(a)