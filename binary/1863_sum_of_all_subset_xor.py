from typing import List
class Solution:
    def subsetXORSum(self,nums:List[int])->int:
        xor_sum = 0 

        for num in nums:
            xor_sum |= num 
        return xor_sum * (1 << len(nums) - 1)
nums = [1,3]
s = Solution() 
print(s.subsetXORSum(nums))