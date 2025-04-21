
def twoSum(nums, target):
    num_map = {}
    
    for i, num in enumerate(nums):
        t = target - num

        if t in num_map:
            return [num_map[t] , i]
        
        num_map[num] = i 

    return None

