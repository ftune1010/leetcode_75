def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    i = j = float("inf")
    for num in nums:
        if num <= i:
            i = num
        elif num <= j:
            j = num
        else:
            return True
    return False

print(increasingTriplet([20,100,10,12,5,13]))