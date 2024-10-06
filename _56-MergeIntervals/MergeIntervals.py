class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        arr=[]
        for i in range(len(intervals)):
            c=i+1
            while(c<len(intervals) and intervals[i][1]>=intervals[c][0] ):
                arr.append([intervals[i][0],intervals[c][1]])
                c=c+1
            if(c<len(intervals) and c==i+1):
                arr.append([intervals[c][0],intervals[c][1]])

        return arr