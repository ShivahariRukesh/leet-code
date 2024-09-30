class Solution(object):

    def maxiNum(self,num1,num2):
        return  num1 if(num1>num2 ) else num2
    def miniNum(self,num1,num2):
        return  num2 if(num1>num2 ) else num1

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if(len(heights)==1):
            return heights[0]
        max=0
        
        for i in range(len(heights)-1):
            min =heights[i]
            for j in range(i+1,len(heights)):
                if(heights[i]==0 and heights[j]==0):
                    max=0
                elif(heights[i]==0 and heights[j]!=0):
                    max=heights[j]

                elif(heights[i]!=0 and heights[j]==0):
                    max=heights[i]
                else:
                    min = self.miniNum(min,heights[j])
                    max=self.maxiNum(max, min*(j-i+1))
                    
        return max