def reverseWords(str):
    words = str.strip().split()

    words.reverse()

    return " ".join(words)

s = "the sky is blue"
print(reverseWords(s))