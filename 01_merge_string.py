def mergeAlternatively(word1, word2):
    w1_len = len(word1)
    w2_len = len(word2)

    shorter_len = min(w1_len, w2_len)
    new_str = ''
    for i in range(0, shorter_len):
        new_str += word1[i]
        new_str += word2[i]
    
    if w1_len > shorter_len:
        new_str += word1[shorter_len:]
    if w2_len > shorter_len:
        new_str += word2[shorter_len:]
    
    return new_str

print(mergeAlternatively('he', 'llo'))