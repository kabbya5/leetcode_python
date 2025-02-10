class Solution:
    def clearDigit(self, s:str)->str:
        stack = [] 

        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

s = Solution()
print(s.clearDigit("cb34"))