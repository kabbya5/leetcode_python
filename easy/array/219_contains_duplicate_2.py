def containsNearbyDuplicated(nums, k):
    num_index = {}

    for i, num in enumerate(nums):
        if num in num_index:
            if i - num_index[num] <= k:
                return True
        num_index[num] = i 

    return False  