def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    if n == 0:
        return True
    bed_length = len(flowerbed)
    for i in range(bed_length):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == bed_length - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
    return False

print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,0,0,1], 2))
