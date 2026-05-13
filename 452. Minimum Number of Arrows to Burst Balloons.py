def findMinArrowShots(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[1])
    last = float("-inf")
    arrows = 0
    for start, end in points:
        if start > last:
            last = end
            arrows += 1            
    return arrows


if __name__ == "__main__":
    points = [[10,16],[2,8],[1,6],[7,12]]
    print(findMinArrowShots(points))
    points = [[1,2],[3,4],[5,6],[7,8]]
    print(findMinArrowShots(points))
    points = [[1,2],[2,3],[3,4],[4,5]]
    print(findMinArrowShots(points))