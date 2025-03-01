def minSubArrayLen(target, nums):
    left = 0 
    sum_window = 0 
    min_length = float('inf')

    for right in range(len(nums)):
        sum_window += nums[right]

        while sum_window >= target:
            min_length = min(min_length, right - left + 1)
            sum_window -= nums[left]
            left += 1 

    return min_length if min_length != float('inf') else 0 

nums = [2,3,1,2,4,3]
target = 7
print(minSubArrayLen(target, nums))