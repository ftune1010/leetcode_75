def combinationSum3(k: int, n: int) -> list[list[int]]:
    res, sol = [], []
    def backtrack(start):
        if len(sol) == k:
            if sum(sol) == n:
                res.append(sol[:])
            return 
        for i in range(start, 10):
            sol.append(i)
            backtrack(i + 1)
            sol.pop()
    backtrack(1)
    return res

if __name__ == "__main__":
    k, n = 3, 7
    print(combinationSum3(k, n))
    k, n = 3, 9
    print(combinationSum3(k, n))
    k, n = 4, 1
    print(combinationSum3(k, n))