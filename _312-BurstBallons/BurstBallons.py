class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        val=0
        while (len(nums)>0):
            min=nums[0]
            index=0
            for i in range(len(nums)):
                if(min>nums[i]):
                    min = nums[i]
                    index=i
            
            a= 1 if (index-1<0) else nums[index-1]

            b = 1 if (index+1>=len(nums)) else nums[index+1]

            val = val+(a*min*b)
            print(val)
            nums.pop(index)
            # nums = nums[0:index] + nums[index+1:len(nums)]

        return val
            
                
                
                    
