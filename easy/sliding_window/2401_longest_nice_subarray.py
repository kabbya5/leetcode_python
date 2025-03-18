
def longestNiceSubarray(nums):
    left = 0 
    mask = 0 
    max_length = 0 

    for right in range(len(nums)):
        while (mask & nums[right])  != 0:
            mask ^= nums[left]
            left += 1 
        mask |= nums[right]
        max_length = max(max_length, right - left + 1)
    
    return max_length

nums = [1, 3, 8, 48, 10]
print(longestNiceSubarray(nums))