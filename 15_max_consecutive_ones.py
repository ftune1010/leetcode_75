def longestOnes(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    l, longest = -1, 0
    for r in range(len(nums)):
        if nums[r] == 0:
            k -= 1
            while k < 0:
                l += 1
                if nums[l] == 0:
                    k += 1
        if longest < r -l:
            longest = r - l
    return longest

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
