def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    from collections import defaultdict, deque
    
    graph = defaultdict(dict)
    for i, val in enumerate(values):
        num, den = equations[i]
        graph[num][den] = val
        graph[den][num] = 1 / val
    #DFS
    def dfs(node:str, target: str, curr: float, visited: set) -> float:
        if node not in graph or target not in graph:
            return -1
        if node == target:
            return 1
        if target in graph[node]:
            return curr * graph[node][target]
        visited.add(node)
        for den, val in graph[node].items():
            if den not in visited:
                result = dfs(den, target, curr * val, visited)
                if result != -1:
                    return result
        return -1
    #DFS
    def bfs(src, target):
        if src not in graph or target not in graph:
            return -1
        queue = deque()
        visited = set([src])
        queue.append([src, 1])

        while queue:
            n, w = queue.popleft()
            if n == target:
                return w
            for conn, weight in graph[n].items():
                if conn not in visited:
                    visited.add(conn)
                    queue.append([conn, w * weight])
        return -1

    return [bfs(num, den) for num, den in queries]

if __name__ == "__main__":
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    print(calcEquation(equations, values, queries))
    equations = [["a","b"],["b","c"],["bc","cd"]]
    values = [1.5,2.5,5.0]
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    print(calcEquation(equations, values, queries))
    equations = [["a","b"]]
    values = [0.5]
    queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    print(calcEquation(equations, values, queries))
