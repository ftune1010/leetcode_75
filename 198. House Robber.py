def rob(nums: list[int]) -> int:
    # Tabulations (Bottom Up Approach)
    n = len(nums)
    for i in range(1, n):
        if i == 1:
            nums[i] = max(nums[i], nums[i - 1])
        else:
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
    return nums[-1]

    # Memoization (Top Down Approach)
    # if n <= 2:
    #     max(nums)
    # memo = {0: nums[0]}
    # def max_loot(x):
    #     if x in memo:
    #         return memo[x]
    #     else:
    #         if x == 1:
    #             memo[1] = max(nums[0], nums[1])
    #         else:
    #             memo[x] = max(nums[x] + max_loot(x - 2), max_loot(x - 1))
    #         return memo[x] 
    # return max_loot(n - 1)

    # Recursive Approach
    # def max_loot(x):
    #     if x == 0:
    #         return nums[0]
    #     if x == 1:
    #         return max(nums[0], nums[1])
    #     return max(nums[x] + max_loot(x - 2), max_loot(x - 1))
    # return max_loot(n - 1)


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(rob(nums))
    nums = [2,7,9,3,1]
    print(rob(nums))
    nums = [2,1,1,2]
    print(rob(nums))