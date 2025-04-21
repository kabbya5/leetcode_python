def gameOfLife(board):
    rows, cols = len(board), len(board[0])

    directions = [(-1,-1), (-1, 0), (-1,1),
                  (0,-1), (0,1),
                  (1,-1), (1,0), (1,1)]
    for r in range(rows):
        for c in range(cols):
            live_neighobrs = 0 
            for dr, dc in directions:
                nr,nc = r + dr, c + dc 
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == 1 or board[nr][nc] == -1:
                        live_neighbors += 1

            if board[r][c] == 1:
                if live_neighobrs < 2 or live_neighobrs > 3:
                    board[r][c] = -1 
            
            else:
                if live_neighobrs == 3:
                    board[r][c] = 2 

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == -1:
                board[r][c] = 0
            elif board[r][c] == 2:
                board[r][c] = 1       