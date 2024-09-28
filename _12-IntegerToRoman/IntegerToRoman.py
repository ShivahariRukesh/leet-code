class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = str(num)
        res=""

        for i in range(len(s)):
            if(len(s)-i==4):
                c=0
                while(c<int(s[i])):
                    res=res+'M'
                    c=c+1
            elif(len(s)-i==3):
                if(int(s[i])<4):
                    c=0
                    while(c<int(s[i])):
                        res=res+'C'
                        c=c+1
                elif(int(s[i])==4):
                    res=res+'CD'
                elif(int(s[i])==9):
                    res=res+'CM'
                else:
                    c=5
                    res=res+'D'
                    while(c<int(s[i])):
                        res=res+'C'
                        c=c+1    
            elif(len(s)-i==2):
                if(int(s[i])<4):
                    c=0
                    while(c<int(s[i])):
                        res=res+'X'
                        c=c+1
                elif(int(s[i])==4):
                    res=res+'XL'
                elif(int(s[i])==9):
                    res=res+'XC'
                else:
                    c=5
                    res=res+'L'
                    while(c<int(s[i])):
                        res=res+'X'
                        c=c+1  
            elif(len(s)-i==1):
                if(int(s[i])<4):
                    c=0
                    while(c<int(s[i])):
                        res=res+'I'
                        c=c+1
                elif(int(s[i])==4):
                    res=res+'IV'
                elif(int(s[i])==9):
                    res=res+'IX'
                else:
                    c=5
                    res=res+'V'
                    while(c<int(s[i])):
                        res=res+'I'
                        c=c+1     

            
        return res
    
a = int(input("Enter the integer\t"))
print("The equivalent roman number to the given integer is\t",Solution().intToRoman(a))    