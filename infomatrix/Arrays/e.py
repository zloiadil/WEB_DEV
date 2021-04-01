n = int(input())

mylist = [int(i) for i in input().split()]

i = 1
ok = False
for i in range(0, len(mylist) - 1):
	if mylist[i]*mylist[i + 1] > 0:
		ok = True
		break

if ok:
	print("YES")
else:
	print("NO")