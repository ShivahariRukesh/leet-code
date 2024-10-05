#Own Solution
class OherSolution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = nums[0:k]
        arr.sort(reverse=True)
        for i in range(k,len(nums)):
            if(arr[-1]<nums[i]):
                arr.pop()
                arr.append(nums[i])
                arr.sort(reverse=True)


        return arr[-1]
    #
    

# Using max-heap to eradicate the exceeding time limit    
class Solution(object):
    def heapify(self,arr,n,i):
        largest=i
        left=(2*i)+1
        right=(2*i)+2
        
        if left<n and arr[left]>arr[largest]:
            largest = left
            
        if right<n and arr[right]>arr[largest]:
            largest = right
            
        if (largest!=i):
            arr[largest],arr[i]= arr[i],arr[largest]
            self.heapify(arr,n,largest)
            
    def findKthLargest(self,nums,k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr= nums    
        n = len(arr)    
        for i in range(n//2-1,-1,-1):
            self.heapify(arr,n,i)
            
        for i in range(n-1,0,-1):
            arr[0],arr[i]= arr[i],arr[0]
            self.heapify(arr,i,0)
        
        return nums[-k]


    


    
n =int(input("Enter the length of an array\t"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter the value for {i+1} position\t")))
k = int(input("Enter the Kth value must be within the length of the Array\t"))
print(f"The {k}th largest value of the given array is\t",Solution().findKthLargest(arr,k))