def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    seen = set()
    # DFS
    def dfs(room):
        seen.add(room)
        for key in rooms[room]:
            if key not in seen:
                dfs(key)
    dfs(0)

    # BFS
    # from collections import deque

    # queue = deque([0])
    # while queue:
    #     room  = queue.popleft()
    #     seen.add(room)
    #     for key in rooms[room]:
    #         if key not in seen:
    #             queue.append(key)

    return len(seen) == len(rooms)



if __name__ == "__main__":
    rooms = [[1],[2],[3],[]]
    print(canVisitAllRooms(rooms))
    rooms = [[1,3],[3,0,1],[2],[0]]
    print(canVisitAllRooms(rooms))
