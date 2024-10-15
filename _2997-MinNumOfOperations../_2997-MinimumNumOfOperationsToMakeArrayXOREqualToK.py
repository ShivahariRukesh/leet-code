class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sol=0
        for i in nums:
            sol = sol ^ i
        count =0
        while(sol>0 or k>0):
            rem1 = sol%2
            rem2 = k%2
            if(rem1!=rem2):
                count=count+1
            sol=sol/2
            k=k/2
        
        return count
            
