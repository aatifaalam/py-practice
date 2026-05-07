s = "anagram"
t = "nagaram"
freq = {} 
def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    for i in s:
        if i in s:
            freq[i] = freq.get(i, 0) + 1
    for i in t:
        if i not in freq:
            return False
        freq[i] = freq[i] - 1
        if freq[i] < 0:
            return False
    return True    

print(valid_anagram(s, t))