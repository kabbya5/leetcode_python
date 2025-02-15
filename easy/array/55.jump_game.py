def canJump(nums):
    maxReach =  0 
    for i in range(len(nums)):
        if i > maxReach:
            return False 
        maxReach = max(maxReach, i + nums[i]) 
        if maxReach >= len(nums) -1:
            return True
        
    return True 

nums = [2, 3, 1, 1, 4]
print(canJump(nums)) 