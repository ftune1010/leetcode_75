def minEatingSpeed(piles: list[int], h: int) -> int:
    left, right = 1, max(piles)
    while left < right:
        k = left + (right - left) // 2
        hours = 0
        for p in piles:
            hours += p // k
            if p % k:
                hours += 1
        if hours <= h:
            right = k
        else:
            left = k + 1
    return left
        
if __name__ == "__main__":
    piles, h = [3,6,7,11], 8
    print(minEatingSpeed(piles, h))
    piles, h = [30,11,23,4,20], 5
    print(minEatingSpeed(piles, h))
    piles, h = [30,11,23,4,20], 6
    print(minEatingSpeed(piles, h))

