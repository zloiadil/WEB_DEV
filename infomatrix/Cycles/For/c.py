import math

a = int(input())
b = int(input())

for x in range(a, b + 1):
    y = math.floor(math.sqrt(x))
    if y * y == x:
        print(x, end=" ")


