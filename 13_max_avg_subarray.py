def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    max_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        new_sum = (max_sum + nums[i] - nums[i - k])
        max_sum = max(new_sum, max_sum)
    return (max_sum / k)

print(findMaxAverage([1,12,-5,-6,50,3], 4))
