def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    from collections import deque

    rows, cols = len(maze), len(maze[0])
    
    queue = deque()
    queue.append(entrance)  # Entrance coordinates plus the number of steps
    maze[entrance[0]][entrance[1]] = "+" # Mark Entrance as seen

    steps = 0
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            for r, c in directions:
                r, c = r + row, c + col
                if 0 <= r < rows and 0 <= c < cols and maze[r][c] == ".":
                    if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                        return steps + 1
                    maze[r][c] = "+"
                    queue.append([r, c])
        steps += 1
    return -1



if __name__ == "__main__":
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]
    print(nearestExit(maze, entrance))
    maze = [["+","+","+"],[".",".","."],["+","+","+"]]
    entrance = [1,0]
    print(nearestExit(maze, entrance))
    maze = [[".","+"]]
    entrance = [0,0]
    print(nearestExit(maze, entrance))
    maze = [
        ["+",".","+","+","+","+","+"],
        ["+",".","+",".",".",".","+"],
        ["+",".","+",".","+",".","+"],
        ["+",".",".",".","+",".","+"],
        ["+","+","+","+","+",".","+"]
        ]
    entrance = [0, 1]
    print(nearestExit(maze, entrance))
