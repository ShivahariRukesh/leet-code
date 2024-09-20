class Solution(object):
    def minWindow(self,s,t):
        if(len(s)<len(t)):
            return ""
        obj={}
        for i in range(len(t)):
            obj[t[i]]=[]
            for j in range (len(s)):
                if(t[i]==s[j]):
                    obj[t[i]].append(j)
        return obj
        
        
obj = Solution()
# s = input("Enter the main string\t")
# t = input("Enter the substring\t")
s='adbccdee'
t='abc'
print(obj.minWindow(s,t))