# Python code to convert string to list
 
def Convert(string):

    li = list(string.split("+"))

    return li
    
def str_to_int(string):
  return  list(map(int,(Convert(string))))
 
# Driver code

str1 = input()

print(Convert(str1))

arr =list(map(int,(Convert(str1))))


ans = sum(arr)

print('result', ans)



	

	




	
	

	
	