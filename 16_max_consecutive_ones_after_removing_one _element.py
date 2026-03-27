def longestSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l, longest= -1, 0
    zero_count = 0
    
    for r in range(len(nums)):
        if nums[r] == 0:                                                                                                                                                        
            zero_count += 1
            while zero_count > 1:
                l += 1
                if nums[l] == 0:
                    zero_count -= 1
        if longest < r - l - 1:
            longest = r - l - 1
    return longest


print(longestSubarray([1,1,0,1]))
print(longestSubarray([0,1,1,1,0,1,1,0,1]))
print(longestSubarray([1,1,1]))



    