class Solution(object):
    def sortMe(self,arr):
        return arr[1]
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals=sorted(intervals,key=self.sortMe)
        

        prev = intervals[0][1]
        count=0
        for i in range(1,len(intervals)):
            if(intervals[i][0]<prev):
                count=count+1
            else:
                prev= intervals[i][1]

    
        return count

arr1 = []
arr2=[]
n = int(input("Enter the length of an array\n"))

for i in range(n):
    for j in range(2):
        arr2.append(int(input(f"Enter for {i+1}th {j+1}th position\n")))
    arr1.append(arr2)
    arr2=[]

print("The required result it\t",Solution().eraseOverlapIntervals(arr1))