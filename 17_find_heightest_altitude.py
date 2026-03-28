def largestAltitude(gain):
    """
    :type gain: List[int]
    :rtype: int
    """
    max_alt = prefix = 0
    for num in gain:
        prefix += num
        if prefix > max_alt:
            max_alt = prefix
    return max_alt

print(largestAltitude([-5,1,5,0,-7]))
print(largestAltitude([-4,-3,-2,-1,4,3,2]))
    