class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        val=0
        for i in range(1,len(s)):
            val = val + abs(ord(s[i])-ord(s[i-1]))

        return val
            

print("The required output of the given string is",Solution().scoreOfString(input(f"Enter the string\t")))