
# Problem Statement 
# You are given two strings, s1 and s2, of equal length. Your task is
# to determine whether you can make the two strings equal by performing 
# at most one swap operation on s1. A swap operation means choosing two 
# different indices in s1 and swapping the characters at those positions. 
# If it is possible to make s1 equal to s2 with exactly one such swap
#  (or if they are already equal), 
# return true; otherwise, return false.

# Algorithm 
# Check if the strings are already equal:

# If s1 == s2, return true immediately since no swap is needed.
# Check if the lengths are different:

# If len(s1) != len(s2), return false since they can never be made equal.
# Find differing positions:

# Iterate through both strings and store the positions where s1[i] != s2[i].
# Evaluate the differences:

# If there are more than two differing positions, return false (because one swap cannot fix more than two mismatches).
# If exactly two differences exist, check if swapping the characters at these positions in s1 makes it equal to s2. If yes, return true, otherwise return false.
# Return false in all other cases.


class Solution:
    def areAlmostEqual(self, s1:str, s2:str)->bool:
        if s1 == s2:
            return True 
        
        if len(s1) != len(s2):
            return False
        
        diff = [(a,b) for a, b  in zip(s1, s2) if a != b]

        return len(diff) == 2 and diff[0] == diff[1][::-1]
    
s = Solution() 

print(s.areAlmostEqual('bank', 'kanb'))
print(s.areAlmostEqual('kelb', 'kelb'))
print(s.areAlmostEqual('attack', 'defend'))
