from typing import List

class Solution:
    def privtArray(self, nums:List[int],pivot:int)->List[int]:
        less_pivot = []
        equal_pivot = []
        getter_pivot = []

        for num in nums:
            if num > pivot:
                 getter_pivot.append(num)
            elif num < pivot:
                less_pivot.append(num)
            else:
                equal_pivot.append(num)

        return less_pivot + equal_pivot + getter_pivot

s = Solution()
print(s.privtArray([9,12,5,10,14,3,10], pivot = 10))