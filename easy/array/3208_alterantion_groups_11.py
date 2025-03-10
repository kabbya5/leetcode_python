def numberOfAlternatingGroups(colors, k):
    n = len(colors)
    ans = 0 
    cur = 1 

    for i in range(1, k + n - 1):
        if colors[i % n] != colors[(i -1) % n]:
            cur += 1 
        else:
            cur = 1 
        if cur == k:
            ans += 1 
            cur -= 1 
    
    return ans
colors = [0,1,0,1,0]
k = 3

print(numberOfAlternatingGroups(colors, k))