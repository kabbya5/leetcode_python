def gridGame(grid):
    n = len(grid[0]) 

    top_sum = [0] * n
    bottom_sum = [0] * n

    top_sum[0] = grid[0][0]
    bottom_sum[0]  = grid[1][0]

    for i in range(1, n):
        top_sum[i] = top_sum[i-1] + grid[0][i] 
        bottom_sum[i] = bottom_sum[i-1] + grid[1][i]

    min_secount_robot_points = float('inf') 

    for i in range(n):
        point_left_top = top_sum[-1] - top_sum[i] 
        points_collected_bottom = bottom_sum[i - 1] if i > 0 else 0 
        secount_robot_points = max(point_left_top, points_collected_bottom)
        min_secount_robot_points = min(min_secount_robot_points, secount_robot_points) 

    return min_secount_robot_points

grid = [
    [2, 5, 4],
    [1, 5, 1]
]

print(gridGame(grid))