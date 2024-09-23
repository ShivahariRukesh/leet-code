class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    return nums[i]

arr=[]
inp = int(input("Enter the size of an array\t"))
print("You have to enter an array of numbers where only one number must be repeated\n")
for i in range(inp):
    arr.append(int(input(f"Enter the num{i+1}\t")))
    
print(Solution().findDuplicate(arr))