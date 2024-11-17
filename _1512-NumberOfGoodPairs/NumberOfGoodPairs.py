class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count =0 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    count+=1

        return count


n = int(input("Enter the length of an array\t"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter the {i+1}th element\t")))
    
print("The required result is\t",   Solution().numIdenticalPairs(arr))