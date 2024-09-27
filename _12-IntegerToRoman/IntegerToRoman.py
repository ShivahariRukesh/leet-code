num= 3800
s = str(num)
res=""

for i in range(len(s)):
    if(len(s)==4):
        c=0
        while(c<int(s[0])):
            res=res+'M'
            c=c+1
    elif(len(s)==3):
        if(int(s[0])<4):
            c=0
            while(c<int(s[0])):
                res=res+'C'
                c=c+1
        elif(int(s[0])==4):
            res=res+'CD'
        elif(int(s[0])==9):
            res=res+'CM'
        else:
            c=5
            res=res+'D'
            while(c<int(s[0])):
                res=res+'C'
                c=c+1            
    s=s[i+1:len(s)]
print(res)            