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
            sol=sol//2
            k=k//2
        print(count)    
        return count
    
    
    
arr1 = []
n = int(input("Enter the length for an array\t"))
for i in range(n):
    arr1.append(int(input(f"Enter the value for {i+1} position\t")))
k = int(input("Enter the value for k\t"))

print("The minimum number of operations to make array XOR equal to K is\t",Solution().minOperations(arr1,k))    
            
