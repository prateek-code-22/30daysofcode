

#Approach 
#We will be checking if substring is palindrome or not.
#if prefix is palindrome then recusively calculate the suffix to be palindrome. 


def partition(s):
        if not s:
            return [[]]
        
        n = len(s)
        
        ans = []
        for i in range(1, n+1):
            # prefix is a palindrome
            if s[:i] == s[:i][::-1]:  
                # process suffix recursively
                for suf in partition(s[i:]):  
                    ans.append([s[:i]] + suf)
        return ans