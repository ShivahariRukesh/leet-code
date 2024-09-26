class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res= [0] * len(temperatures)
        stack=[]
        for i in range (len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                res[stack.pop()]=i - stack[-1]
            stack.append(i)
        return res

n = int(input("Enter the length for an array of temperatures\t")    )
arr=[]
for i in range(n):    
    arr.append(input(f"Enter for temperature {i+1}\t"))   
    
print("The number of days you have to wait for the hight hotness than the current for the provided array of temperature is\t",Solution().dailyTemperatures(arr))    
     