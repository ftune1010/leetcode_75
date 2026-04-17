def minFlips(a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: int
    """
    flips = 0
    while (a or b):
        count = 0
        if a & 1:
            count += 1
        if b & 1:
            count += 1
        if c & 1:
            if count == 2:
                count = 0
            else:
                count -= 1
        flips += abs(count)
        print(flips)
        a >>= 1
        b >>= 1
        c >>= 1

    return flips

# print(minFlips(2, 6, 5))
print(minFlips(8, 3, 5))
# print(minFlips(4, 2, 7))
# print(minFlips(1, 2, 3))
# print(minFlips(7, 7, 7))
print([].pop())
