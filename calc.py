
result =0
def ref_calc(x,y,oparator):
	
	if oparator == "+":
	   result = int(x)+int(y)
	   print(result)
	    

print('Enter calc in x :')

x = input() 
oparator = input() 
y = input()

ref_calc(x,y,oparator)
