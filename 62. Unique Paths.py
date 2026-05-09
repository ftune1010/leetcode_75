def uniquePaths(m: int, n: int) -> int:
    # Recursive Approach
    # def paths(i, j):
    #     if i == j == 0:
    #         return 1
    #     if i < 0 or i == m or j < 0 or j == n:
    #         return 0
    #     return paths(i - 1, j) + paths(i, j - 1)
    # return paths(m - 1, n - 1)

    # Memoization
    # memo = {(0, 0): 1}
    # def paths(i, j):
    #     if (i, j) in memo:
    #         return memo[(i, j)]
    #     if i < 0 or j < 0 :
    #         return 0
    #     memo[(i, j)] = paths(i - 1, j) + paths(i, j - 1)
    #     return memo[(i, j)]
    # return paths(m - 1, n - 1)

    # Tabulation
    # grid = [[1] * n for _ in range(m)]
    # for i in range(1, m):
    #     for j in range(1, n):
    #         grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
    # return grid[m - 1][n - 1]

    row = [1] * n
    for _ in range(m - 1):
        for j in range(1, n):
            row[j] += row [j - 1]
    return row[-1]

if __name__ == "__main__":
    m, n = 3, 7
    print(uniquePaths(m, n))
    m, n = 3, 2
    print(uniquePaths(m, n))
    