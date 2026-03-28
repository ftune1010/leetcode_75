def equalPairs(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    from collections import defaultdict
    
    n = len(grid)
    pairs = 0
    row_counts = defaultdict(int)
    
    for row in grid:
        row_counts[tuple(row)] += 1
    for i in range(n):
        column = tuple(grid[j][i] for j in range(n))
        if column in row_counts:
            pairs += row_counts[column]
    return pairs


print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))