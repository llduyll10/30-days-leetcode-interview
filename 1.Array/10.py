def jump(nums):
    n = len(nums)
    if n <= 1:
        return 0

    jumpCount = 0
    farthest = 0
    currentEnd = 0

    for i in range(n-1):
        farthest = max(farthest, i+nums[i])

        if i == currentEnd:
            jumpCount += 1
            currentEnd = farthest

            if currentEnd >= n-1:
                break

    return jumpCount

nums = [2,3,1,1,4]
print(jump(nums))