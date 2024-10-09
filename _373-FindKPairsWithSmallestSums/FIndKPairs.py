class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        sum=[]
        for i in nums1:
            for j in nums2:
                sum.append([i,j])
        print(sum)
        return sum[0:k]
    

arr1 = []
arr2=[]

n1= int(input("Enter the size of first array\t"))
for i in range(n1):
    arr1.append(int(input(f"Enter the value in {i+1} position\t")))
    
n1= int(input("Enter the size of second array\t"))
for i in range(n1):
    arr2.append(int(input(f"Enter the value in {i+1} position\t")))
    
k = int(input("Enter the K value\t"))
    
print(f"The {k}pairs with Smallest Sums is\n",Solution().kSmallestPairs(arr1,arr2,k))