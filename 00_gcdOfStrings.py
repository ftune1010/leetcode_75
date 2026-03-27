def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
        
    def get_gcd(a, b):
        while b:
            a, b = b, a % b
        return a
        
    gcd_len = get_gcd(len(str1), len(str2))                                                                                                             
    return str1[:gcd_len]


print(gcdOfStrings('ABCABC', 'ABC'))
print(gcdOfStrings('ABABAB', 'ABAB'))
print(gcdOfStrings('LEET', 'CODE'))
print(gcdOfStrings('TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXX'))
