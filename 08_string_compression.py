def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    i = insert = 0
    while (i < len(chars)):
        group = 1
        while (group + i) < len(chars) and chars[i] == chars[group + i]:
            group += 1
        chars[insert] = chars[i]
        insert += 1
        if group > 1:
            group_string = str(group)
            chars[insert: insert + len(group_string)] = list(group_string)
            insert += len(group_string)
        i += group
    return insert

print(compress(["a"]))