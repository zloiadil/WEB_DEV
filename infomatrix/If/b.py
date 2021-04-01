import math

year = int(input())

result = None

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    result = "YES"
else:
    result = "NO"

print(result)
