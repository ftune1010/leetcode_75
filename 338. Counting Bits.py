def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        res[i] = res[i//2] + i%2
    
    # offset = 1
    # for i in range(1, n + 1):
    #     if offset * 2 == i:
    #         offset = i
    #     res[i] = 1 + res[i - offset]
    return res

print(countBits(5))