
# My Own -Time Limit Exceeded 
class AnotherSolution(object):

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
        
        max=heights[0]
        for i in range(len(heights)-1):
            min =heights[i]
            
            for j in range(i+1,len(heights)):
                max=self.maxiNum(heights[j],max)
                if(heights[i]==0 and heights[j]==0):
                    min = 0
                    max=self.maxiNum(0,max)
                elif(heights[i]==0 and heights[j]!=0):
                    min = 0
                    max=self.maxiNum(heights[j],max)

                elif(heights[i]!=0 and heights[j]==0):
                    min=0
                    max=self.maxiNum(heights[i],max)
                else:
                    min = self.miniNum(min,heights[j])
                    max=self.maxiNum(max, min*(j-i+1))
                    
        return max
    
    # Time Limit Exceeded
    
    
    
    # The one submitted on leetcode using concept of monostack
    
    
class Solution(object):

    def maxiNum(self,num1,num2):
        return  num1 if(num1>num2 ) else num2


    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max=0
        stack=[]
        stack.append({"index":0,"height":heights[0]})
        for i in range(1,len(heights)):
            c=-1

            while((len(stack)!=0) and (heights[i]<stack[-1]["height"])):
                newIndex = stack[-1]["index"]
                max = self.maxiNum(stack[-1]["height"]*(i-newIndex),max)
                stack.pop()
                c=0
            if(c==0):
                stack.append({"index":newIndex,"height":heights[i]})
            else:
                stack.append({"index":i,"height":heights[i]})

        
        while(len(stack)!=0):
            max =  self.maxiNum(max, stack[-1]["height"]*(len(heights)-stack[-1]["index"]) )
            stack.pop()




        print(max)
                    
        return max 
    
    
n = int(input("Enter the length of array\t"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter the value for rectangle {i+1}\t")))
    
print("The largest rectangle in the histogram is\t",Solution().largestRectangleArea(arr))