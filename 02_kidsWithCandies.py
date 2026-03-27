def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """

    max_no_of_candy = max(candies)
    result = []
    for candy in candies:
        if candy + extraCandies >= max_no_of_candy:
            result.append(True)
        else:
            result.append(False)
    return result

print(kidsWithCandies([2,3,5,1,3], 3))
print(kidsWithCandies([4,2,1,1,2], 1))
print(kidsWithCandies([12, 1, 12], 10))