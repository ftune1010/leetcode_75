def maxVowels(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    vowels = 'aeiou'
    max_v = 0
    for i in range(k):
        if s[i] in vowels:
            max_v += 1
    
    curr_v = max_v
    for i in range(k, len(s)):
        curr_v += 1 if s[i] in vowels else 0
        curr_v -= 1 if s[i - k] in vowels else 0
        if curr_v > max_v:
            max_v = curr_v
    return max_v


print(maxVowels("abciiidef", 3))
print(maxVowels("aeiou", 2))
print(maxVowels("leetcode", 3))
 