from collections import defaultdict
from itertools import permutations
def permute(nums):
    # return list(permutations(nums))
    def generate_permutations(li):
        if len(nums) == len(li):
            result.append(li.copy())

        for n in nums:
            if taken[n]:
                continue 
            taken[n] = True 

            generate_permutations(li + [n])
            taken[n] = False 

    taken = defaultdict(bool)
    result = []

    generate_permutations([])

    return result 


nums = [1,2,3]
print(permute(nums))