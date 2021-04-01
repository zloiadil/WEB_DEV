a = int(input())

mylist = [int(i) for i in input().split()]

pos = 0
for x in mylist:
	if x > 0:
		pos += 1
		#print(x)

print(pos)