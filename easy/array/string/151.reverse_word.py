class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])



s = Solution()

s1 = "the sky is blue"
s2 = "  hello world  "
s3 = "a good   example"

print(s.reverseWords(s1))
print(s.reverseWords(s2))
print(s.reverseWords(s3))