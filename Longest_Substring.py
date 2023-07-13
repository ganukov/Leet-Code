s = 'abcabcbb'
char_dict = {}
start = 0
length = 0

for i in range(len(s)):
    if s[i] in char_dict:
        start = max(start, char_dict[s[i]] + 1)
    char_dict[s[i]] = i
    length = max(length, i - start + 1)

print(length)