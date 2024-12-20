import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=0
        temp=abs(x)
        rev=0
        
        while (temp!=0):
            
            a=temp%10
            rev= rev*10+a
            temp=temp//10


        if -rev < -2**31 or rev > 2**31 - 1:
            return 0
        else:

            if x<0:
                return -rev
            else:
                return rev
            


print("The desired result is",Solution().reverse(int(input("Enter the integer\t"))))            
        