class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        while(i+1<len(nums) and (nums[i]<nums[i+1])):
            i=i+1

        if(target>nums[i]):
            return -1
        else:
            if(target<nums[0]):
                a=i+1
                b=len(nums)-1
            else:
                a=0
                b=i
                
            s=target
            value=None
            while(a<=b):
                m = (a+b)//2
                
                if (nums[m]>s):
                    b=m-1
                elif (nums[m]==s):
                    value =m
                    break
                else:
                    a=m+1
            if(value>-1):
                return value
            else:
                return -1
arr1=[]
n = int(input("Enter the length of the list\t"))

print("Please enter the rotated sorted list\n")
for i in range(n):
    arr1.append(int(input(f"Enter the {i+1}th element\t")))


    
print("The index of the searached element is",Solution().search(arr1,int(input("Enter the element you want to search\t"))),"\tBut if you get output -1 it means the searched index is not there in the given list")