from typing import List

def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
    n = len(grid)

    nums = [num for row in grid for num in row]
    count = [0] * (n * n + 1)

    repated, missing = - 1, -1,

    for num in nums:
        count[num] += 1 

    for i in range(1, n * n + 1):
        if count[i] == 2:
            repated = i 

        elif count[i] == 0:
            missing = i 
        
    return [repated, missing]

grid = [[9,1,7],[8,9,2],[3,4,6]]
print(findMissingAndRepeatedValues(grid))