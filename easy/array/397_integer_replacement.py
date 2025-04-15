from collections import defaultdict 

def integerReplacement(n):
    min_operation = 0

    def operation(n):
        if n == 1:
            return 0
        
        if n % 2 == 0:
           return 1 + operation(n//2)
        
        ops1 = operation(n - 1)
        ops2 = operation(n + 1)
        return 1 + min(ops1, ops2)

    cache = defaultdict(int)

    return count_ops(n)

n = 7

print(integerReplacement(n))