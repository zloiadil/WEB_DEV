a = int(input())

mylist = [int(i) for i in input().split()]

for x in mylist:
	if x % 2 == 0:
		print(x)