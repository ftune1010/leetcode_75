def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    last = float("-inf")
    overlaps = 0
    for start, end in intervals:
        if start >= last:
            last = end
        else:
            overlaps += 1
    return overlaps

if __name__ == "__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print(eraseOverlapIntervals(intervals))
    intervals = [[1,2],[1,2],[1,2]]
    print(eraseOverlapIntervals(intervals))
    intervals = [[1,2],[2,3]]
    print(eraseOverlapIntervals(intervals))
    intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
    print(eraseOverlapIntervals(intervals))


