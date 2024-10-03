class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = nums[0:k]
        arr.sort(reverse=True)
        for i in range(k,len(nums)):
            if(arr[-1]<nums[i]):
                arr.pop()
                arr.append(nums[i])
                arr.sort(reverse=True)


        return arr[-1]
    
    
n =int(input("Enter the length of an array\t"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter the value for {i+1} position\t")))
k = int(input("Enter the Kth value must be within the length of the Array\t"))
print(f"The {k}th largest value of the given array is\t",Solution().findKthLargest(arr,k))