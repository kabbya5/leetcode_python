from collections import defaultdict
class Solution:
    def maximumSum(self, nums:list[int])->int:

        def sum_of_digits(n):
            return sum(int(d) for d in str(n))
        

        digits_sum_map = defaultdict(list) 
        max_sum  = - 1

        for num in nums:
            digits_sum = sum_of_digits(num)
            digits_sum_map[digits_sum].append(num)

        for key in digits_sum_map:
            if len(digits_sum_map[key]) > 1:
                top_two = sorted(digits_sum_map[key], reverse=True)[:2] 
                max_sum = max(max_sum, sum(top_two))
        
        return max_sum
    
s = Solution()
nums = [18, 43, 36, 13, 7]
print(s.maximumSum(nums))