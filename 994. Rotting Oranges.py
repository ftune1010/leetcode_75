def orangesRotting(grid: list[list[int]]) -> int:
    from collections import deque
    
    EMPTY, FRESH, ROTTEN = 0, 1, 2

    rows, cols = len(grid), len(grid[0])
    fresh =  minutes = 0
    queue = deque()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == FRESH:
                fresh += 1
            elif grid[i][j] == ROTTEN:
                queue.append((i, j))
            else:
                pass

    while queue and fresh > 0:
        for _ in range(len(queue)):
            row, col  = queue.popleft()
            directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for r, c in directions:
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == FRESH:
                    grid[r][c] = ROTTEN
                    fresh -= 1
                    queue.append((r, c))
        minutes += 1
    return minutes if fresh == 0 else -1
    

if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(orangesRotting(grid))
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(orangesRotting(grid))
    grid = [[0,2]]
    print(orangesRotting(grid))


