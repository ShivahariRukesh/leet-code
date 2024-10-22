class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        small=0
        big=0
        for i in s:
            if(i==')' or i=="("):
                small+=1
            else:
                big +=1

        if(small%2==0 and big%2==0):
            return True
        else:
            return False
        
