class Solution(object):

    def minWindow(self,s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        lenT = len(t)
        lenS = len(s)
        
        if( lenS<lenT):
            return ""
        obj={}
        temp = lenT 
        k=""
        a=""
        while(temp<=lenS):
            for i in range(lenS-temp+1):
                a= s[i:temp+i]
                re=a
                k=""
                for j in range(lenT):
                    # is_found = re.find(t[j])
                    if (t[j] in re):
                        re= re.replace(t[j],'',1)
                        k= k+t[j]
                    else:
                        k=k+'3neil' 
                if(k==t):
                    i=lenS*2
                    temp=lenS+1
                    break
            temp=temp+1
        return a
    
    

        
obj = Solution()
# s = input("Enter the main string\t")
# t = input("Enter the substring\t")
s='adbccdee'
t='abcc'
print(obj.minWindow(s,t))