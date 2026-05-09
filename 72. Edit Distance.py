from pprint import pprint


def minDistance(word1: str, word2: str) -> int:
    w1, w2 = len(word1) + 1, len(word2) + 1
    dp = [[0] * w1 for _ in range(w2)]
    for j in range(1, w1):
        dp[0][j] = j
    for i in range(1, w2):
        dp[i][0] = i
    for i in range(1, w2):
        for j in range(1, w1):
            if word1[j - 1] == word2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    pprint(dp)
    return dp[i][j]



if __name__ == "__main__":
    word1, word2 = "horse", "ros"
    print(minDistance(word1, word2))
    word1, word2 = "intention", "execution"
    print(minDistance(word1, word2))