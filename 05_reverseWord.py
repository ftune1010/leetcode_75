def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        words[:] = [words[x] for x in range(len(words) - 1, -1, -1) if words[x] != '']
        return " ".join(words)

print(reverseWords("the sky is blue"))