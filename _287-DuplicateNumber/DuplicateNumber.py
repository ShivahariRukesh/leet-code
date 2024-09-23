# 1. Owin soluting Using tuple logic doesn't show time limit exceeded

# class Solution(object):
#     def findDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

#         temp =set()
#         for i in range(len(nums)):
#             if (nums[i] in temp):
#                 return nums[i]
#             temp.add(nums[i])
#         return       

# 2. By using Floyd's cycle detection algorithm (Tortoise and Hare)          

# class Solution(object):
#     def findDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         tortoise = nums[0]
#         hare = nums[0]

#         while(True):
#             hare = nums[nums[hare]]
#             tortoise =nums[tortoise]
#             if (hare==tortoise):
#                 break
#         tortoise = nums[0]

#         while(hare != tortoise):
#             hare = nums[hare]
#             tortoise = nums[tortoise]

#         return hare

# 3 Own solution but with time limit 
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