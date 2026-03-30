def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    stack = []
    for ast  in asteroids:
        while stack and ast < 0 and stack[-1] > 0:
            last = stack.pop()
            if last > abs(ast):
                stack.append(last)
                break
            elif abs(ast) == last:
                break
        else:
            stack.append(ast)
    return stack


print(asteroidCollision([5,10,-5]))
print(asteroidCollision([8,-8]))
print(asteroidCollision([10,2,-5]))
print(asteroidCollision([3,5,-6,2,-1,4]))
print(asteroidCollision([-2,1,1,-1]))