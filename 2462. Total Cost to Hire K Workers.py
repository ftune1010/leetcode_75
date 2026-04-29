def totalCost(costs: list[int], k: int, candidates: int) -> int:
    import heapq
    
    heap1, heap2 = [], []
    i, j =  0, len(costs) - 1
    ans = 0
    while k:
        k -= 1
        while len(heap1) < candidates and i <= j:
            heapq.heappush(heap1, costs[i])
            i += 1
        while len(heap2) < candidates and j >= i:
            heapq.heappush(heap2, costs[j])
            j -= 1
        c1 = heap1[0] if heap1 else float("inf")
        c2 = heap2[0] if heap2 else float("inf")
        if c1 <= c2:
            ans += heapq.heappop(heap1)
        else:
            ans += heapq.heappop(heap2)
    return ans

if __name__ == "__main__":
    costs = [17,12,10,2,7,2,11,20,8]
    k = 3
    candidates = 4
    print(totalCost(costs, k, candidates))
