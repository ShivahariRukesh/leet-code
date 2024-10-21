class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        f,l=0,len(nums)-1
       
        if(nums[f]<nums[l]):
            min= nums[0]
        else:
            min = nums[l]

        while(f<=l):
            mid = (f+l)//2
 
            if(min>nums[mid]):
                min = nums[mid]
            if(nums[f]<nums[mid]):
                f= mid+1
                if(min>nums[f]):
                    min = nums[f]
        
            else:
                l = mid-1
                if(min>nums[l]):
                    min= nums[l]
                  

        return min


arr1=[]
n = int(input("Enter the length of the list\t"))

print("Please enter the rotated sorted list\n")
for i in range(n):
    arr1.append(int(input(f"Enter the {i+1}th element\t")))


    
print("The smallest number from the given array is\t",Solution().findMin(arr1))