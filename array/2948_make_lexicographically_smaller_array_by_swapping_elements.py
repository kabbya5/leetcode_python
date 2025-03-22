def make_smallest_array(arr, k):
    n = len(arr)

    for i in range(n):
        limit = min(i + k + 1, n) 
        min_idx = 1 
        for j in range(i + 1, limit):
            if arr[j] < arr[min_idx]:
                min_idx =j
arr = [7, 6, 9, 2, 1]
k = 3
result = make_smallest_array(arr, k)
print(result)   