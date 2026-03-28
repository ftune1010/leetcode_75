def closeStrings(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: bool
    """
    from collections import defaultdict

    if len(word1) != len(word2):
        return False
    if set(word1) != set(word2):
        return False
        
    dict_1 = defaultdict(int)
    dict_2 = defaultdict(int)
    for i in range(len(word1)):
        dict_1[word1[i]] += 1
        dict_2[word2[i]] += 1
    return sorted(dict_1.values()) == sorted(dict_2.values())


print(closeStrings('abc', 'bca'))
print(closeStrings('abcde', 'abcde'))
print(closeStrings('a', 'aa'))
print(closeStrings('cabbba', 'abbccc'))