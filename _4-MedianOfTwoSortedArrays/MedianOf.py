class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums2 = nums1+nums2
        nums2.sort()
        med = (float(len(nums2)+1))/2  
        intMed = int (med)
        if(intMed != med):
            return (float(nums2[intMed-1]+nums2[intMed])/2)
        else:
            return float(nums2[intMed-1])
        
obj1 = Solution()

arr1=[]
arr2=[]
for j in range(2):
    arrSize1 = int(input(f"Enter the size for Array{j+1}\t"))
    for i in range(arrSize1):
        x=float(input(f"Enter for {i+1}\t"))
        arr1.append(x)
    arr2.append(arr1)    

print("Median of two array is",obj1.findMedianSortedArrays(arr2[0],arr2[0]))
    
        