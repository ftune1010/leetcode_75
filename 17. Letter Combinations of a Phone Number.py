def letterCombinations(digits: str) -> list[str]:
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        }
    n = len(digits)
    combinations = []

    def backtrack(curr, index):
        if index == n:
            combinations.append(curr)
            return
        for letter in phone[digits[index]]:
            backtrack(curr + letter, index + 1)
    backtrack("", 0)
    return combinations

    # Iterative approach (BFS)
    # combinations = [""]
    # for digit in digits:
    #     sol = []
    #     for combo in combinations:
    #         for letter in phone[digit]:
    #             sol.append(combo + letter)
    #     combinations = sol      
    # return combinations


if __name__ == "__main__":
    digits = "23"
    print(letterCombinations(digits))