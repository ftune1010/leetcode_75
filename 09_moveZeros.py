def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    insert = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[insert], nums[i] = nums[i], nums[insert]
            insert += 1
    print(nums)

moveZeroes([0,1,0,3,12])
