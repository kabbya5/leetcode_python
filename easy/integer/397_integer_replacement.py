def integerReplacement(n):
    steps = 0 

    while n != 1:
        if n % 2 == 0:
            n = n // 2 
        else:
            if n == 3:
                n -= 1 
            elif (n + 1) % 4 == 0:
                n += 1 
            else:
                n -= 1 
        steps += 1 
    
    return steps 
n = 4

print(integerReplacement(n))