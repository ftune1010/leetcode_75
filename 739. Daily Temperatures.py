def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    ans, stack = [0] * n, []

    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            index = stack.pop()
            ans[index] = i - index
        stack.append(i)
    return ans


if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(temperatures))
    temperatures = [30,40,50,60]
    print(dailyTemperatures(temperatures))
    temperatures = [30,60,90]
    print(dailyTemperatures(temperatures))
