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
        
            if c<nums[i]:
                arr.append([c,count])
                c=nums[i]
                count =1
                
            else:
                count =count+1
        arr.append([c,count])
        def sortMe(val):
            return val[1]
        arr.sort(key=sortMe,reverse=True)

        for i in range(0,k):
            arr[i]= arr[i][0]

        return arr[0:k]


arr = []

n = int(input(f"Enter the size of an array\t"))
for i in range(n):
    arr.append(int(input(f"Enter the number {i+1}\t")))
k = int(input(f"Enter the Kth value(it must be small or equals to the unique numbers in an array\t"))

print("The most frequent repeated top K numbers are\t",Solution().topKFrequent(arr,k))