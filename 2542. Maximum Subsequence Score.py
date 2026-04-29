def maxScore(nums1: list[int], nums2: list[int], k: int) -> int:
    import heapq

    pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
    pairs.sort(key=lambda x: x[1], reverse=True)

    heap = []
    max_score = curr_sum = 0
    for n1, n2 in pairs:
        curr_sum += n1
        heapq.heappush(heap, n1)

        if len(heap) > k:
            curr_sum -= heapq.heappop(heap)
        if len(heap) == k:
            max_score = max(max_score, curr_sum * n2)
    return max_score

if __name__ == "__main__":
    nums1 = [1,3,3,2]
    nums2 = [2,1,3,4]
    k = 3
    print(maxScore(nums1, nums2, k))
    nums1 = [4,2,3,1,1]
    nums2 = [7,5,10,9,6]
    k = 1
    print(maxScore(nums1, nums2, k))
