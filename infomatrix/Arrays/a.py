a = int(input())

mylist = [int(i) for i in input().split()]

i = 0
for x in mylist:
	if i % 2 == 0:
		print(x)
	i += 1