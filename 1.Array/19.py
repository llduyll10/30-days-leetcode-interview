def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while s.find(prefix) != 0:
            prefix = prefix[:-1] #loại bỏ ký tự cuối cùng
            if not prefix:
                return ""
    return prefix
print(longestCommonPrefix(["flower", "flow", "flight"]))
