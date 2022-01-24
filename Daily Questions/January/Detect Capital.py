#Noob code:
#check if s[0] and s[1] is capital then rest must be capital.
#if s[0] is capital then rest are small(lowercase)
#if s[0] is small then rest character must be small.

def detectCapital(s):
        n = len(s)
        
        if len(s)==1:
            return True
        
        #if s[0] is uppercase
        if 65 <= ord(s[0]) <=90:

            #if s[1] is also upper case then no lowercase should be present.(ex: USA)
            if 65 <= ord(s[1]) <=90:
                for i in range(2,n):
                    #No lowercase character
                    if 97<= ord(s[i]) <=122:
                        return False

            #if s[0] is upper case then No upper case is allowed, all must be lowercase (ex:Google) 
            else:
                for i in range(1,n):
                    #No uppercase letters
                    if 65<= ord(s[i]) <=90:
                        return False

        #all lowercase should be persent(ex:leetcode)
        else:
            for i in range(1,n):
                    if 65<= ord(s[i]) <=90:
                        return False
        
        return True