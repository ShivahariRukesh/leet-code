class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res = [-1] * len(nums1)


        for i in range(len(nums1)):
            foundIndex=nums2.index(nums1[i])
            
            if(foundIndex):
                for j in range(foundIndex+1,len(nums2)):
                    print(nums1[i],nums2[j])
                    if(nums1[i]<nums2[j]):
                        res[i]=nums2[j]
                        break

        return res    