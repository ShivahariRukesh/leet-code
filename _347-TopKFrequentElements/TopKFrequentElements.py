class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr=[]
        count=0
        nums.sort()
        c=nums[0]

        if(nums[0]==nums[-1] ):
            return [nums[0]]

        for i in range(len(nums)):
        
            if c<nums[i] or :
                arr.append([c,count])
                c=nums[i]
                count =0
                continue
            else:
                count =count+1
        print(arr)
        def sortMe(val):
            return val[1]
        arr.sort(key=sortMe,reverse=True)

        for i in range(0,k):
            arr[i]= arr[i][0]
        return arr



        