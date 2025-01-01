class Solution:
    def maxScore(self, s: str) -> int:
        totalOnes = s.count('1') 
        leftZeros = 0
        maxScore = 0 

        for i in range(len(s) - 1):
            if s[i] == '0':
                leftZeros += 1
            else:
                totalOnes -= 1
            
            maxScore = max(maxScore, leftZeros + totalOnes)

        return maxScore


s = Solution()
print(s.maxScore("011101")) 
print(s.maxScore("00111")) 
print(s.maxScore("1111")) 