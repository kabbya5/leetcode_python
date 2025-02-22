from typing import List 

class Solution:
    def canCompleteCircuit(self,gas:List[int], cost:List[int])->int:
        total_gas, total_cost = sum(gas), sum(cost) 

        if total_gas < total_cost:
            return - 1 
        
        start, tank = 0, 0 

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0 


        return start 
    
gas = [3,1,1]
cost = [1,2,2]

s = Solution() 
print(s.canCompleteCircuit(gas,cost))

         