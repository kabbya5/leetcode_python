from collections import Counter
def longestPalindrome(s: str) -> str:
    ans = ''
    def palindrome(start,char):
        end = start
        while(start < len(s)):
            if s[end] == char:
                new_s = s[start:end]
                if new_s == new_s[::-1]:
                    ans = max(ans, new_s)
                    return 
            end +=1 
            
    char_count = Counter(s)

    for i, char in enumerate(s):
        if char_count[char] > 1:
            palindrome(i,char)

    return ans

s1 = "babad"
s2 = "cbbd"

print(longestPalindrome(s1))
print(longestPalindrome(s2))