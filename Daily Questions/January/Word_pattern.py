
def wordPattern(self, pattern: str, str1: str) -> bool:
        n = len(pattern)
        dic = {}
        words = str1.split(' ')
        m = len(words)

        #if len is not equal
        if n!=m:
            return False
        
        if len(set(pattern)) != len(set(words)):
             return False

        else:
            for i in range(n):
                if pattern[i] not in dic:
                    dic[pattern[i]] = words[i]
                elif dic[pattern[i]]!=words[i]:
                        return False

        return True




pattern = "abba"
str1 = "dog cat dog cat"
print(wordPattern(pattern,str1))

