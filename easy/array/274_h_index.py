def hIndex(citations):
    n = len(citations)
    count = [0] * (n + 1)

    for c in citations:
        if c >= n:
            count[n] += 1
        else:
            count[c] += 1

    total = 0
    for h in range(n, -1, -1):
        total += count[h]
        if total >= h:
            return h
    return 0

citations = [3, 0, 6, 1, 5]
print(hIndex(citations))