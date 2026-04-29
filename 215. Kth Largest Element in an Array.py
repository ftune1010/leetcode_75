def findKthLargest(nums: list[int], k: int) -> int:
    # Using sort
    # nums.sort()
    # return nums[len(nums) - k]

    import heapq
    # Using max heap
    # for i in range(len(nums)):
    #     nums[i] = -nums[i]
    # heapq.heapify(nums)

    # for _ in range(k - 1):
    #     heapq.heappop(nums)
    # return -nums[0]

    # Using min heap
    heap = []
    for n in nums:
        if len(heap) < k:
            heapq.heappush(heap, n)
        else:
            heapq.heappushpop(heap, n)
    return  heap[0]
    

    # quick select
    # k = len(nums) - k
    # def quick_select(l, r):
    #     pivot, p = nums[r], l
    #     for i in range(l, r):
    #         if nums[i] <= pivot:
    #             nums[p], nums[i] = nums[i], nums[p]
    #             p += 1
    #     nums[p], nums[r] = nums[r], nums[p]
    #     if p == k:
    #         return nums[p]
    #     elif p > k:
    #         return quick_select(l, p - 1)
    #     else:
    #         return quick_select(p + 1, r)

    # return quick_select(0, len(nums) - 1)

if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print(findKthLargest(nums, k))
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(findKthLargest(nums, k))