class Solution(object):

    def maxNum(self,num1,num2):
        return num1 if num1>num2 else num2
    
    def minNum(self,num1,num2):
        return num1 if num1<num2 else num2

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        n=len(intervals)
        i=0
        arr=[]
        while i<n and intervals[i][1]<newInterval[0]:
            arr.append(intervals[i])
            i=i+1
   

     
        min = newInterval[0]
        max = newInterval[1]

        while i<n and intervals[i][0]<=newInterval[1]:
            min = self.minNum(min,intervals[i][0])
            max = self.maxNum(max,intervals[i][1])
            i=i+1

        arr.append([min,max])

        while i<n:
            arr.append([intervals[i][0],intervals[i][1]])
            i=i+1
        return arr

            

