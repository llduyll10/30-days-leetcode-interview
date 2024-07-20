def isPalindrome(s):

    filteredChar = []

    for char in s:
        if char.isalnum():
            filteredChar.append(char.lower())

    left, right = 0, len(filteredChar)-1

    while left < right:
        if filteredChar[left] != filteredChar[right]:
            return False

        left += 1
        right -= 1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))