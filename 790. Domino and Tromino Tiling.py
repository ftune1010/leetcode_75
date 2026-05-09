def numTilings(n: int) -> int:
    MOD = 10 ** 9 + 7
    if n <= 2:
        return n
    prev2, prev1, curr = 1, 1, 2
    for i in range(3, n + 1):
        prev2, prev1, curr = prev1, curr, 2 * curr + prev2
    return curr % MOD



if __name__ == "__main__":
    n = 5
    print(numTilings(n))