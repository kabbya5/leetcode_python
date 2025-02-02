class Solution:
    def isArraySepecial(self, nums:list[int]) ->bool:
        for i in range(1, len(nums)):
            if nums[i] %2 == nums[i -1] % 2:
                return False 
        return True
    
s = Solution()
print(s.isArraySepecial([1]))
print(s.isArraySepecial([2,1,4]))
print(s.isArraySepecial([4,3,4,6]))