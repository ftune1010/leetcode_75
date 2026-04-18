def minReorder(n: int, connections: list[list[int]]) -> int:
    from collections import deque, defaultdict

    neighbors = defaultdict(list)
    edges = set()
    for start, end in connections:
        neighbors[start].append(end)
        neighbors[end].append(start)
        edges.add((start, end))
    
    visited = set([0])
    reversals = 0

    #DFS
    def dfs(city):
        nonlocal reversals
        for neighbor in neighbors[city]:
            if neighbor not in visited:
                if (neighbor, city) not in edges:
                    reversals += 1
                visited.add(neighbor)
                dfs(neighbor)
    dfs(0)

    # BFS
    # queue = deque([0])
    # while queue:
    #     for _ in range(len(queue)):
    #         city = queue.popleft()
    #         for neighbor in neighbors[city]:
    #             if neighbor not in visited:
    #                 visited.add(neighbor)
    #                 queue.append(neighbor)
    #                 if (neighbor, city) not in edges:
    #                     reversals += 1
    return reversals


if __name__ == "__main__":
    n, connections = 6, [[0,1],[1,3],[2,3],[4,0],[4,5]]
    print(minReorder(n, connections))
    n, connections = 5, [[1,0],[1,2],[3,2],[3,4]]
    print(minReorder(n, connections))
    n, connections = 3, [[1,0],[2,0]]
    print(minReorder(n, connections))