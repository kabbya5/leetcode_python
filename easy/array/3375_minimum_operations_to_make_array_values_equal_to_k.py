def min_operations(nums,k):
    if num in nums:
        if num < k:
            return - 1 
        
        greater_than_k = set() 

        for num in nums:
            if num > k:
                greater_than_k.add(num)

        return len(greater_than_k)