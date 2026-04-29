import random

def guessNumber(n: int) -> int:
    ans = random.randint(1, n)

    l = 1
    r = n
    def guess(num: int):
        if ans == num:
            return 0
        elif ans < num:
            return -1
        else:
            return 1
        
    while l < r:
        num = l + (r - l) // 2
        pick = guess(num)
        if pick == 0:
            return num
        elif pick == -1:
            r = num - 1
        else:
            l = num + 1
    return l

if __name__ == "__main__":
    n = 10
    print(guessNumber(n))