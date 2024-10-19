class Solution(object):
    def revInver(self,val):
        newVal=""
        for i in range(len(val)):
            if(val[i]=='0'):
                newVal = newVal + '1'
            else:
                newVal = newVal+ '0'
        
        againVal=""
        for i in range(len(newVal)):
            againVal = newVal[i]+againVal
            
        return againVal

    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        arr=[]
        arr.append("0")
        for i in range(1,n):
            arr.append(arr[i-1] + "1" + self.revInver(arr[i-1]) )
        
        return(arr[n-1][k-1])
        