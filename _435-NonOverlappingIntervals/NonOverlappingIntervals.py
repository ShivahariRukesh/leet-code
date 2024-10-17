class Solution(object):
    def sortMe(self,arr):
        return arr[1]
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        sorted(intervals,key=self.sortMe)

        # print(intervals)
        prev = intervals[0][1]
        count=0
        for i in range(1,len(intervals)):
            if(intervals[i][0]<prev):
                count=count+1
            else:
                prev= intervals[i][1]


        print(count)
        return count
