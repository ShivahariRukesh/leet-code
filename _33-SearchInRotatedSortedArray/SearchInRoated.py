#First trying to implement binary search
arr1=[1,2,3,4,5,6]

a = 0
b=len(arr1)-1
s=6
value=None
for i in range(len(arr1)):
    if(arr1[a]==s):
        value = a
        break
    if(arr1[b]==s):
        value = b
        break
   
    
        
    
    m = (a+b)//2
    if (arr1[m]>s):
        b=m
    elif (arr1[m]==s):
        value =m
        break
    else:
        a=m
        
if(value):
    print(value+1)
else:
    print("Not found")
        