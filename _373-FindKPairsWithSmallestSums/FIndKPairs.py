## Time Limit Exceeded
class Solution1(object):
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
class Solution2(object):
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
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """    
        if not nums1 or not nums2 or k == 0:
            return []
        
        def heapify(arr, n, i):
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            # If left child is smaller than root
            if left < n and (arr[left][0] + arr[left][1] < arr[smallest][0] + arr[smallest][1]):
                smallest = left

            # If right child is smaller than the smallest so far
            if right < n and (arr[right][0] + arr[right][1] < arr[smallest][0] + arr[smallest][1]):
                smallest = right

            # If smallest is not root
            if smallest != i:
                arr[i], arr[smallest] = arr[smallest], arr[i]
                heapify(arr, n, smallest)

        # Min-heap to store (nums1[i], nums2[0], i, 0) where nums1[i] + nums2[0] is the current smallest pair
        heap = []

        # Add the first pair from each nums1[i] with nums2[0]
        for i in range(min(k, len(nums1))):
            heap.append([nums1[i], nums2[0], i, 0])

        for x in range(len(heap) // 2 - 1, -1, -1):
            heapify(heap, len(heap), x)

        result = []

        # Extract the k smallest pairs
        while heap and len(result) < k:
            smallest_pair = heap[0]
            result.append([smallest_pair[0], smallest_pair[1]])

            # Get next pair (nums1[i], nums2[j + 1]) by advancing in nums2
            i, j = smallest_pair[2], smallest_pair[3]
            if j + 1 < len(nums2):
                heap[0] = [nums1[i], nums2[j + 1], i, j + 1]
                heapify(heap, len(heap), 0)
            else:
                # Remove the element if no further pairs can be formed
                heap[0], heap[-1] = heap[-1], heap[0]
                heap.pop()
                for x in range(len(heap) // 2 - 1, -1, -1):
                    heapify(heap, len(heap), x)

        return result
arr1 = []
arr2=[]

n1= int(input("Enter the size of first array\t"))
print("The values should be entered in an ascending order\n")
for i in range(n1):
    arr1.append(int(input(f"Enter the value in {i+1} position\t")))
    
n1= int(input("Enter the size of second array\t"))
for i in range(n1):
    arr2.append(int(input(f"Enter the value in {i+1} position\t")))
    
k = int(input("Enter the K value\t"))
    
print(f"The {k}pairs with Smallest Sums is\n",Solution().kSmallestPairs(arr1,arr2,k))