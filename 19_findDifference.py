def findDifference(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    """
    set_1 = set(nums1)
    set_2 = set(nums2)
    diff = set_1.symmetric_difference(set_2) # set1 ^ set2
    res = [[], []]

    for val in diff:
        if  val in set_1:
            res[0].append(val)
        if val in set_2:
            res[1].append(val)
    
    return res

print(findDifference([1,2,3], [2,4,6]))
print(findDifference([1,2,3,3], [1,1,2,2]))


    