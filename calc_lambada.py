import math

values = True

def ref_calc_add(x,y):
  
       	    return (int(x)+int(y))

def ref_calc_sub(x,y):
            
              return  (int(x)-int(y))
              
def ref_calc_multi(x,y):
            
              return  (int(x)*int(y))
              
def ref_calc_div(x,y):
            
              return  (int(x)/int(y))
          
def ref_calc_mv2(x,y):
	           
	           return  (int(x)*(int(y)**2))




oparator =input()
a = input()
b= input()

if oparator =="+":
	print(ref_calc_add(a,b))

elif oparator =="-":
    		print(ref_calc_sub(a,b))
 
elif oparator =="*":
    		print(ref_calc_multi(a,b))
    		
elif oparator =="/":
    		if a >b :
    			print(ref_calc_div(a,b))
    	    
elif oparator == "/":
    		if a<b:
    			print(ref_calc_div(a,b))

elif oparator =="mv2":
	   print (ref_calc_mv2(a,b))
	   
	 # min max   														   
min = min(a,b)
print(min)
max = max(a,b)
print(max)
