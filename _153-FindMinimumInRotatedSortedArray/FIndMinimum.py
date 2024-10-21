#Completed in O(n) time

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while(i+1<len(nums) and nums[i]<nums[i+1]):
            i=i+1
        
        if(i==len(nums)-1):
            return nums[0]
        else:
            return nums[i+1]

#