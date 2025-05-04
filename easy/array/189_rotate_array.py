def rotate(nums, k):
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
    n = len(nums)
    k %= n 

    reverse(0,n -1)
    reverse(0, k-1)
    reverse(k, n-1)

    return nums
    
nums = [1,2,3,4,5,6,7]
k = 3

print(rotate(nums, k))