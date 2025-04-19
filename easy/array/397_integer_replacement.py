from collections import defaultdict 

def integerReplacement(n):
    min_operation = 0

    def operation(n):
        if n == 1:
            return 0
        
        if cache[n]:
            return cache[n]
        
        if n % 2 == 0:
            cache[n//2] = operation(n//2)
            cache[n] = 1 + cache[n//2]
            return cache[n]
           
        cache[n+1] = operation(n - 1)
        cache[n-1] = operation(n - 1)
        cache[n] = 1 + min(cache[n+1], cache[n-1])
        return cache[n]

    cache = defaultdict(int)

    return operation(n)

n = 7

print(integerReplacement(n))