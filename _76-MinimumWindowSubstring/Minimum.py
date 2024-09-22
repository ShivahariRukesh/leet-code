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
                        k=k+'?'
                if(k==t):
                    
                    i=lenS*2
                    temp=lenS+1
                    break
            temp=temp+1
        if(k==t):
            return a    
        return "" 
    
    

        
obj = Solution()
s = input("Enter the main string\t")
t = input("Enter the substring\t")
print(obj.minWindow(s,t))