def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    s_list = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    i = 0
    j = len(s) - 1

    while i < j:
        while i < j and s_list[i] not in vowels:
            i += 1
        while i < j and s_list[j] not in vowels:
            j -= 1
        s_list[i], s_list[j] = s_list[j], s_list[i] 
        i += 1
        j -= 1
    return "".join(s_list)


print(reverseVowels("IceCreAm"))
print(reverseVowels("leotcede"))