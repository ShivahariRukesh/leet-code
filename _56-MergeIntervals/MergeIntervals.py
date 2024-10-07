class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        def sortFirstIndex(val):
            return val[0]
        arr=[]
        sortedArr = sorted(intervals,key=sortFirstIndex)
        arr.append([sortedArr[0][0],sortedArr[0][1]])
        for i in range(1,len(sortedArr)):
            if(arr[-1][1]>=sortedArr[i][0]):
            
                if(arr[-1][1]<sortedArr[i][1]):
                    arr[-1]=[arr[-1][0],sortedArr[i][1]]
                else:
                    arr[-1]=[arr[-1][0],arr[-1][1]]
            
            else:
                arr.append([sortedArr[i][0],sortedArr[i][1]])

        return arr
    

    
n=int(input(f"Enter the length of an array\t"))
arr=[]
for i in range(n):
    a=int(input(f"Enter the first value for position {i+1}\t"))
    b=int(input(f"Enter the second value for position {i+1}\t"))
    arr.append([a,b])

print("The merged interval of the given array is \t",Solution().merge(arr))