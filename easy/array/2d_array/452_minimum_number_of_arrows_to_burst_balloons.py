def findMinArrowShots(points):
    if not points:
        return 0 
    
    points.sort(key=lambda x:x[1])

    arrows = 1 

    end = points[0][1]

    for start, stop in points[1:]:
        if start > end:
            arrows += 1 
            end = stop 

    return arrows
        

points = [[10,16],[2,8],[1,6],[7,12]]

print(findMinArrowShots(points))