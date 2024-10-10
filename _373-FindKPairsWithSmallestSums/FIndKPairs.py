## Time Limit Exceeded
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        def sortMe(val):
            return val[0]+val[1]

        for i in nums1:
            for j in nums2:
                sum.append([i,j])
        

        sum.sort(key=sortMe)
        
        return sum[0:k]
##
# Memory Limit Exceeded    
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        arr=[]
        for i in nums1:
            for j in nums2:
                arr.append([i,j])

        def heapMe(arr,n,i):
            
            l = i
            left = 2*i+1
            right = 2*i+2
            
            if(left <n and ((arr[left][0]+arr[left][1])>(arr[l][0]+arr[l][1]))):
                l=left
            if(right <n and ((arr[right][0]+arr[right][1])>(arr[l][0]+arr[l][1]))):
                l=right
            
            if l!=i:
                arr[l],arr[i] = arr[i],arr[l]
                heapMe(arr,n,l)
        n =len(arr)    
        for i  in range(n//2-1,-1,-1):
            heapMe(arr,n,i)
            
        for i in range(n-1,0,-1):
            arr[0],arr[i] = arr[i],arr[0]
            heapMe(arr,i,0)
            
            
        return arr[0:k]
##
    

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