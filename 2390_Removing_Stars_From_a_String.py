def removeStars(s):
    """
    :type s: str
    :rtype: str
    """
    stack  = []
    for item in s:
        if item == "*":
            if stack:
                stack.pop()
        else:
            stack.append(item)
    return "".join(stack)

print(removeStars("leet**cod*e"))
print(removeStars("erase*****"))