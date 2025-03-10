from typing import List
import math 
def closestPrimes(left:int, right:int)->List[int]:
    def seive(n):
        is_prime = [True] * (n + 1) 
        is_prime[0] = is_prime[1] = False 

        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i*i, n+1, i):
                    is_prime[j] = False 
                    print(i,j)

        return is_prime 

    is_prime = seive(right) 
    primes = [i for i in range(left, right + 1) if is_prime[i]]
    min_gap = float('inf')
    closest_pair = [-1, -1]

    for i in range(len(primes) - 1):
        gap = primes[i + 1] - primes[i] 
        if gap < min_gap:
            min_gap = gap 
            closest_pair = [primes[i], primes[i + 1]] 
    
    return closest_pair

print(closestPrimes(2,8))
