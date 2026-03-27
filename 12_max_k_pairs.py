def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # i = j = ops = 0                   ###Time limit exceeded
    # while i < len(nums):
    #     j = i + 1
    #     while j < len(nums):
    #         if nums[i] + nums[j] == k:
    #             ops += 1
    #             nums.pop(i)
    #             nums.pop(j - 1)
    #             i = j = 0
    #         j += 1
    #     i += 1
    # return ops
    from collections import defaultdict
    
    pairs  = 0
    dic = defaultdict(int)

    for num in nums:
        if dic[k - num] > 0:
            pairs += 1
            dic[k - num] -= 1
        else:
            dic[num] += 1
    return pairs

print(maxOperations([1, 2, 3, 4], 5))
print(maxOperations([3,1,3,4,3], 6))