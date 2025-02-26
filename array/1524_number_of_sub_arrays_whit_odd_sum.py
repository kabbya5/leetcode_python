from typing import List 

class Solution:
    def numOfSubarrays(self, arr:List[int])->int:
        odd_count = 0 
        event_count = 1 
        curr_sum = 0 
        result = 0 
        MOD = 10 ** 9 + 7 

        for num in arr:
            curr_sum += num 
            if curr_sum % 2 == 0:
                result += odd_count
                event_count += 1
            else:
                result += event_count 
                odd_count += 1 
            
            result %= MOD

        return result; 

s = Solution()
print(s.numOfSubarrays([1,3,5]))