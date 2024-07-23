def lengthOfLongestSubstring(s):
    start = 0
    maxLength = 0
    chars = set()

    for end in range(len(s)):
        while s[end] in chars:
            chars.remove(s[start])
            start += 1
        chars.add(s[end])
        maxLength = max(maxLength, end - start + 1)
    return maxLength

s = "abcabcbb"
print(lengthOfLongestSubstring(s))