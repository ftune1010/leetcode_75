def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    if n <= 2:
        return min(cost, default=0)
    prev = cost[0]
    curr = cost[1]
    for i in range(2, n):
        prev, curr = curr, min(prev, curr) + cost[i] 
    return min(prev, curr)


if __name__ == "__main__":
    cost = [10,15,20]
    print(minCostClimbingStairs(cost))
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(minCostClimbingStairs(cost))