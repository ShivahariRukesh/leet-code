class Solution(object):
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
    


# Using max-heap to eradicate the exceeding time limit    
arr =[1,-7,3,2,6,0,-8]
sort =[]


def heapae(arr):
    for i in range(len(arr)):
        c=i+1
        while(c>0):
          if(arr[c-1]<arr[i]):
              temp = arr[c-1]
              arr[c-1]=arr[i]
              arr[i]=temp
              break
          c=c//2
    return arr
       
arr =heapae(arr)

while(arr and len(arr)):
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1]=temp
    
    sort.append(arr.pop())
    
    heapae(arr)
   
print(sort)   

# Using max heap sort

    
n =int(input("Enter the length of an array\t"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter the value for {i+1} position\t")))
k = int(input("Enter the Kth value must be within the length of the Array\t"))
print(f"The {k}th largest value of the given array is\t",Solution().findKthLargest(arr,k))