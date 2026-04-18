def findCircleNum(isConnected: list[list[int]]) -> int:
    rows, cols = len(isConnected), len(isConnected[0])
    visited = set()
    provinces = 0

    def dfs(i: int):
        for j in range(cols):
            if j not in visited and isConnected[i][j]:
                visited.add(j)
                dfs(j)

    for i in range(rows):
        if i in visited:
            continue
        visited.add(i)
        provinces += 1
        for j in range(cols):
            if j not in visited and isConnected[i][j]:
                visited.add(j)
                dfs(j)
        
    return provinces



if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(findCircleNum(isConnected))
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(findCircleNum(isConnected))