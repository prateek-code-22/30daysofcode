def atoi(s):
        #remove whitespaces
        s=s.lstrip() 

        #sign bit 
        negative=False

        #empty string 
        if not s:
            return 0

        #if '-' is present     
        if s[0]=="-":
            negative=True
            s=s[1:]

        #if neg not present    
        elif s[0]=="+":
            negative=False
            s=s[1:]


        ans=0
        
        for i in s:
            #if not digit
            if i not in '0123456789':
                break
            else:
                ans=ans*10+int(i)
        
        if negative:
            ans=-ans
        return max(min(ans,2**31 -1),-2**31)
        