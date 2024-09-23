class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        obj= {}
        sum=0
        p=n
        
        while (n!=1 and n not in obj):
            sum=0
            while(n!=0):
                sum = sum + (n%10)**2
                n=n//10
            obj[p] = ""
            p = sum
            n=sum
   
        print(obj)
        return n==1


print(Solution().isHappy(int(input("Enter a number\t"))))