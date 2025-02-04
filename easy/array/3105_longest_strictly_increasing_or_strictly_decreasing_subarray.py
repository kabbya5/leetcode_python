class Solution:
    def longestMomotonicSubarray(self, nums:list[int])->int:
        if not nums:
            return 0 
        
        inc_len = 1 
        dec_len = 1 
        max_len = 1 

        for i in range(1, len(nums)):
            if(nums[i] > nums[i - 1]):
                inc_len += 1
                dec_len  = 1 
            elif nums[i] < nums[i - 1]:
                dec_len += 1 
                inc_len = 1 
            else:
                inc_len = 1 
                dec_len = 1 

            max_len = max(max_len, inc_len, dec_len) 

        return max_len 

s = Solution() 
print(s.longestMomotonicSubarray([1, 3, 5, 4, 2, 8, 10, 9])) 
print(s.longestMomotonicSubarray([10, 9, 8, 7, 6, 5])) 
print(s.longestMomotonicSubarray([5, 6, 7, 8, 2, 1, 4, 3])) 
print(s.longestMomotonicSubarray([1, 2, 2, 3]))