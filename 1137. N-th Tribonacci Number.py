def tribonacci(n: int) -> int:
    #  Recursive solution
    # if n == 0:
    #     return 0
    # if n <= 2:
    #     return 1
    # return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-2)
    
    # Top Down Approach Space: O(n) Time: O(n)
    # memo = {0: 0, 1: 1, 2: 1}
    # def tri(x):
    #     if x in memo:
    #         return memo[x]
    #     else:
    #         memo[x] = tri(x - 1) + tri(x - 2) + tri(x - 3)
    #         return memo[x]
    # return tri(n)
    
    # Bottom Up Approach Space: O(n) Time: O(n)
    # if n == 0:
    #     return 0
    # if n <= 2:
    #     return 1
    # tri = [0] * (n + 1)
    # tri[1] = tri[2] = 1
    # for i in range(3, n + 1):
    #     tri[i] = tri[i - 1] + tri[i - 2] + tri[i - 3]
    # return tri[n]

    # Bottom Up Approach Space: O(1) Time: O(n)
    if n == 0:
        return 0
    if n <= 2:
        return 1
    first, second, third = 0, 1, 1
    for _ in range(3, n + 1):
        first, second, third = second, third, first + second + third
    return third


if __name__ == "__main__":
    n = 3
    print(tribonacci(n))
    n = 10
    print(tribonacci(n))