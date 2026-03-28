def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    from collections import defaultdict

    num_dict = defaultdict(int)
    for i in arr:
        num_dict[i] += 1

    count = set()
    for value in num_dict.values():
        if value in count:
            return False
        count.add(value)
    return True


print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([1,2]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
    