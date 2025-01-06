def minOperations(boxes: str) -> list[int]:
    n = len(boxes)
    answer = [0] * n
    count = 0 
    opearation = 0
    for  i in range(n):
        answer[i] += opearation 
        if boxes[i] == '1':
            count += 1
        opearation += count
    count = 0
    opearation = 0
    
    for i in range(n-1, -1, -1):
        answer[i] += opearation 
        if boxes[i] == '1':
            count += 1
        opearation += count

    

boxes = "110"
print(minOperations(boxes))