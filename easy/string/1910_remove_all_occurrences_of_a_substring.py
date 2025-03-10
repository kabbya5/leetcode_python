class Solution:
    def removeOccurrences(self, s:str, part:str)->str:
        n = len(s) 
        k = len(part)
        t = [''] * n 
        j = 0 

        for i, c in enumerate(s):
            t[j] = c 
            j += 1 
            if j >= k and ''.join(t[j-k:j]) == part:
                j -= k 
        
        return '' .join(t[:j])
    

    def removeOccurrences2(self,s:str, part:str)->str:
        while part in s:
            s = s.replace(part,"", 1)
        
        return s 
    

s1 = "daabcbaabcbc"
part = "abc"

s = Solution()
print(s.removeOccurrences(s1,part))
print(s.removeOccurrences2(s1,part))