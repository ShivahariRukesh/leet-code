class Solution(object):

    def maxNum(self,num1,num2):
        return num1 if num1>num2 else num2
    
    def minNum(self,num1,num2):
        return num1 if num1<num2 else num2

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        print(intervals,newInterval)
        n=len(intervals)
        i=0
        arr=[]
        while i<n and intervals[i][1]<newInterval[0]:
            arr.append(intervals[i])
            i=i+1
   

     
        min = newInterval[0]
        max = newInterval[1]

        while i<n and intervals[i][0]<=newInterval[1]:
            min = self.minNum(min,intervals[i][0])
            max = self.maxNum(max,intervals[i][1])
            i=i+1

        arr.append([min,max])

        while i<n:
            arr.append([intervals[i][0],intervals[i][1]])
            i=i+1
        return arr
    
    
arr1 = []
arr12=[]
arr2=[]

n1= int(input("Enter the size of an interval\t"))
print("The values should be entered in an ascending order\n")
for i in range(n1):
    for j in range(2):
        arr12.append(int(input(f"Enter the value in {i+1} row and {j+1} column position\t")))
        
    arr1.append(arr12)
    arr12=[]
print("Enter the new interval in ascending order\n")
for j in range(2):
    arr2.append(int(input(f"Enter the value for {j+1} position\t")))
    
    
print(f"The required output is\n",Solution().insert(arr1,arr2))

            

