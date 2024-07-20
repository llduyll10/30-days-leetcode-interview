def lengthOfLastWord(s):
    s = s.strip()

    words = s.split(" ")

    return(len(words[-1]))

s =  "luffy is still joyboy"
print(lengthOfLastWord(s))