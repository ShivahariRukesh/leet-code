class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr=[]

        for i in range(0,len(s)):
            temp=""
            for j in range(i,len(s)):
                if(s[j] in temp): 
                    arr.append(temp)  
                    break
                else:         
                    temp = temp+s[j]
                    if(j==len(s)-1):
                        arr.append(temp)
               
        if(len(arr)==0):
            return 0

        max=arr[0]

        for i in range(1,len(arr)):
            if(len(max)<len(arr[i])):
                max=arr[i]    
        return len(max)        


sol =  Solution()

print(sol.lengthOfLongestSubstring("pppq"))

