class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paranthStack=[]
        for i in range(len(s)):
            if(s[i]=="(" or s[i]=="[" or s[i]=="{"):
                paranthStack.append(s[i])
            elif(s[i]==")"):
                if(paranthStack and paranthStack[-1]=="(" ):
                    paranthStack.pop()            
                else:
                    return False
            elif(s[i]=="]"):
                if(paranthStack and paranthStack[-1]=="[" ):
                    paranthStack.pop()                  
                else:
                    return False

            elif(s[i]=="}"):
                if(paranthStack and paranthStack[-1]=="{" ):
                    paranthStack.pop()                  
                else:
                    return False
        return not paranthStack
        
print("The entered parantheses is\t",Solution().isValid(input("Enter the parantheses [{()}]\t"))," as a valid one ")