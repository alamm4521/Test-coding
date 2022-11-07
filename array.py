

text1 = input().strip()
text2 = input().strip()



x = int(len(text1))
y = int(len(text2))

#print(x)

swap = 0
temp = 0
temp1 = ''

#print (type(swap))
#print(type(temp))


#print(type(x))
#print(type(y))

## test
while x != 0:
	swap = int(text1[x-1])+int(text2[y-1])
	
	
	
	x = x -1
	y = y - 1


print(swap)