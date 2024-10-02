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