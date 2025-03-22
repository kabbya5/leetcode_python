def canPlaceFlowers(flowerbed, n):
    count = 0 
    length = len(flowerbed) 

    for i in range(length):
        if flowerbed[i] == 0:
            right = (i == length -1) or (flowerbed[i+1] == 0)
            left = (i == 0) or (flowerbed[i - 1] == 0)

            if left and right:
                flowerbed[i] = 1 
                count += 1 
                if count >= n:
                    return True 
    return count >= n 

print(canPlaceFlowers([1,0,0, 1],1))
print(canPlaceFlowers([1, 0, 0, 0, 1], 1))