class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=0
        temp=abs(x)
        rev="0"
        
        while (temp!=0):
            a=temp%10
            rev= rev+str(a)
            temp=temp/10

        if x<0:
            return -int(rev)
        else:
            return int(rev)