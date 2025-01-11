from collections import Counter

class Solution:
    def canConstruct(self, s:str, k:int)->bool:
        char_count = Counter(s)

        odd_count = sum(freq % 2 for freq in char_count.values())

        return k <= len(s) and k >= odd_count 

st = Solution()
s = "annabelle"
k = 2
s2 = "leetcode"
k2 = 3
s3 = "true"
k3 = 4
print(st.canConstruct(s,k))
print(st.canConstruct(s2,k2))
print(st.canConstruct(s3,k3))