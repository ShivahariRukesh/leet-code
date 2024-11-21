class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sum=0
        
        for i in range(len(s)):
            c=0
            while(s[i]!=t[c]):
                c=c+1
            
            sum = sum+(((i-c)**2)**0.5)
            
            
        return int(sum)
    
print("Enter two strings below\n")
print(f"the permutation difference between the  is equal to :",Solution().findPermutationDifference(input("Enter a first string\t"),input("Enter a second string\t")))
