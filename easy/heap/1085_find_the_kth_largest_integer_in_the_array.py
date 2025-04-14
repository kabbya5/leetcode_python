import heapq 
def kthLargestNumber(nums,k):
    minHeap = [] 

    for num in nums:
        heapq.heappush(minHeap,int(num))
        if len(minHeap) > k:
            heapq.heappop(minHeap)
        
    return str(minHeap[0])

nums = ["3","6","7","10"]
k = 4
print(kthLargestNumber(nums, k))