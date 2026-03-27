def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    
    i = max_area = 0
    j = len(height) - 1
    while i < j:
        area = min(height[i], height[j]) * (j - i)
        if area > max_area:
            max_area = area
        if height[i] >= height[j]:
            j -= 1
        else:
            i += 1
    return max_area
    
print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
