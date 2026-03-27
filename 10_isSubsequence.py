def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    ptr_s = ptr_t = 0
    while ptr_s < len(s) and ptr_t < len(t):
        if s[ptr_s] == t[ptr_t]:
            ptr_s += 1
        ptr_t += 1
    return ptr_s == len(s)

print(isSubsequence("axc", "ahbgdc"))
    