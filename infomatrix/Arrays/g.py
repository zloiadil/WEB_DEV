import math
n = int(input())

arr = [int(i) for i in input().split()]

for i in range(0, math.floor(len(arr)/2)):
	arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]


for i in range(0, len(arr)):
	print(arr[i])