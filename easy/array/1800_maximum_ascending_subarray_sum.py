# The problem "1800. Maximum Ascending Subarray Sum" asks us to 
# find the maximum sum of a contiguous subarray where
# the elements are strictly increasing.
# Example 1
# Input:
# nums = [10, 20, 30, 5, 10, 50]

# Output:
# 65

# Approach
# Iterate through the array while keeping track of the current sum of the ascending subarray.
# If the current element is greater than the previous one, add it to the sum.
# Otherwise, reset the sum to the current element.
# Keep track of the maximum sum encountered.

class Solution:
    def maxAscendingSum(self, nums:list[int])->int:
        if not nums:
            return False
        n = len(nums) 
        max_sum = nums[0]
        asc_sum = nums[0]

        for i in range(1,n):
            if nums[i] > nums[i - 1]:
                asc_sum += nums[i]
            else:
                asc_sum = nums[i]
            
            max_sum = max(max_sum, asc_sum)
        
        return max_sum 

s = Solution()
print(s.maxAscendingSum([10, 20, 30, 5, 10, 50]))  # Output: 65
print(s.maxAscendingSum([10, 20, 30, 40, 50]))    # Output: 150
print(s.maxAscendingSum([12, 17, 15, 13, 10, 11, 12]))  # Output: 33