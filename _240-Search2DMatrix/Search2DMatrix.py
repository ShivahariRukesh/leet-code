# By Using this method it didn't create any limit exceed error too
class newSolution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            for j in i:
                if(j==target):
                    return True

        return False
    
    
    # Using the concept of modified binary searching algorithm
    
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if(i[0]<=target and target<=i[-1]):
                
                a=0
                b=len(i)
                while(a<=b):
                    mid = (a+b)//2
                    if(i[mid]==target):
                        return True
                    elif(i[mid]<target):
                        a=mid+1
                    else:
                        b=mid-1


        return False
    

arr1=[]
arr2=[]
target= int(input("Enter the num you want to  searcht"))
n =int(input(f"Enter the length for the 2D array\t"))
for i in range(n):
    for j in range(5):
        arr1.append(int(input(f"Enter for the position {i+1}{j+1}\t")))
    arr2.append(arr1)
    arr1=[]

print("The value you searched is ",Solution().searchMatrix(arr2,target))