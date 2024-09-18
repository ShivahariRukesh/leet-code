class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sumVal = float (sum(nums[:k]))
        maxVal = sumVal/k

        for i in range(len(nums)-k):
            sumVal = sumVal - nums[i]+nums[i+k]
            avgVal = sumVal/k
            if(maxVal<avgVal):
                maxVal = avgVal

        return maxVal
    
obj1 = Solution()

arr=[]
userIn = int(input("Enter the size of array\t"))
for i in range(userIn):
    arr.append(int(input(f"Enter the {i+1} positioned element\t")))
    
k = int(input("Now, please enter the value for the K\t"))   
        
print("The answer is \n",obj1.findMaxAverage(arr,k))
    