# # Problem Explanation
# # You're given an integer array, and you need to find all valid tuples (a, b, c, d) such that:
# # axb = cxd 
# # where a, b, c, and d are distinct (i.e., they come from different indices).

# Solution Approach
# Count Pair Products:

# First, generate all possible pairs (a, b) and compute their product.
# Store these products in a hashmap (dictionary) to track how many times each product appears.
# If a product appears more than once, it means we found valid tuples.
# How Many Tuples Can We Form?
# .
# Each pair contributes 8 different valid tuples (since numbers can be arranged in multiple ways).

from collections import defaultdict 

def tupleSameProduct(nums):
    product_map = defaultdict(int) 
    n = len(nums) 
    count = 0 

    for i in range(i + 1, n):
        for j  in range(i + 1, n):
            product = nums[i]  * nums[j] 
            count += product_map[product]
            product_map[product] += 1
     
    return count * 8 