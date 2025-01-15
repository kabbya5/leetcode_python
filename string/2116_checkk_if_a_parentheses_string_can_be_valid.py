class Solution:
    def canBeValid(self, s:str, locked:str)-> bool:
        if(len(s) % 2 != 0):
            return False
        
        low, high, = 0, 0

        for i in range(len(s)):
            if locked[i] == '0': 
                low = max(0, low - 1)
                high += 1

            elif s[i] == '(':
                low += 1
                high += 1
            else:  
                low = max(0, low - 1)
                high -= 1
            if high < 0:
                return False
        return low == 0

sl = Solution()
s = "))()))"
locked = "010100"
print(sl.canBeValid(s,locked))