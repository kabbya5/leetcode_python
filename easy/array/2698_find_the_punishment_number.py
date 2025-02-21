class Solution:
    def canPertition(self,s,target, index = 0, current_sum =0):
        if index == len(s):
            return current_sum == target
        num = 0 
        for i in range(index, len(s)):
            num = num * 10 + int(s[i])
            if current_sum + num > target:
                break
            if self.canPertition(s, target, i + 1, current_sum + num):
                return True
        return False

    def punishmentNumber(self, n:int)-> int:
        total = 0 
        for x in range(1, n + 1):
            square_str = str(x * x) 
            if self.canPertition(square_str,x):
                total += x * x 

        return total

s = Solution()
print(s.punishmentNumber(50))