a = int(input())

mylist = [int(i) for i in input().split()]

i = 0
ans = 0
while i < a - 1:
	x = mylist[i]
	y = mylist[i + 1]
	if y > x:
		ans += 1
	i += 1

print(ans)