def findSubstring(s, words):
    wordLen = len(words[0])
    numsWord = len(words)
    totalLen = wordLen * numsWord
    wordCount = {}

    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    result = []

    for i in range(len(s) - totalLen + 1):
        seen = {}

        for j in range(numsWord):
            wordIndex = i + j * wordLen
            word = s[wordIndex: wordIndex+wordLen]

            if word not in wordCount:
                break

            if word in seen:
                seen[word] += 1
            else:
                seen[word] = 1

            if seen[word] > wordCount[word]:
                break
            if j + 1 == numsWord:
                result.append(i)

    return result

s = "foofoothefoobarman"
words = ["foo", "foo"]
print(findSubstring(s, words))
