class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        arr1=[]
        arr2=[]
        for i in range(1,n+1):
            if(i<m):
                arr1.append(i)
            else:
                if(i%m==0):
                    arr2.append(i)
                else:
                    arr1.append(i)


        return sum(arr1)-sum(arr2)


print(f"The difference of the sum of divisble numbers from the sum of non divisible numbers is\t",Solution().differenceOfSums(int(input("Enter a max range number\t")),int(input("Enter a number to check its divisibility"))))