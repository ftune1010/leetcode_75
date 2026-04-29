def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    potions.sort()
    n = len(spells)
    m = len(potions)
    pairs = [0] * n
    
    def binary_search(spell):
        left = 0
        right = m
        while left < right:
            mid = left + (right - left) // 2
            if spell * potions[mid] >= success:
                right = mid
            else:
                left = mid + 1
        return m - left

    for i, s in enumerate(spells):
        pairs[i] = binary_search(s)
    return pairs


if __name__ == "__main__":
    spells = [5,1,3]
    potions = [1,2,3,4,5]
    success = 7
    print(successfulPairs(spells, potions, success))
    spells = [3,1,2]
    potions = [8,5,8]
    success = 16
    print(successfulPairs(spells, potions, success))

