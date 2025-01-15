from collections import Counter

class Solution:
    def minimumLenght(self, s:str)->int:
        count = Counter(s)

        return sum(2 if freq % 2 == 0 else 1 for freq in count.values())

st = Solution()
s="abaacbcbb"
print(st.minimumLenght(s))