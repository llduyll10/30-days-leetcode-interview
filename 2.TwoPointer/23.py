def isSubsequence(s, t):
    pointerS , pointerT = 0, 0
    lenS, lenT = len(s), len(t)

    while pointerS < lenS and pointerT < lenT:
        if s[pointerS] == t[pointerT]:
            pointerS += 1
        pointerT += 1
    return lenS == pointerS
print(isSubsequence("abc", "ahbgdc"))