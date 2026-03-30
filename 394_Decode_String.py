def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    for i in range(len(s)):
        if s[i] == "]": 
            char = ""
            while stack and stack[-1] != "[":
                char = stack.pop() + char
            stack.pop()
            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(char * int(k))
        else:
            stack.append(s[i])
    return "".join(stack)


print(decodeString("3[a]2[bc]"))
print(decodeString("3[a2[c]]"))
print(decodeString("2[abc]3[cd]ef"))
print(decodeString("100[leetcode]"))
print(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))