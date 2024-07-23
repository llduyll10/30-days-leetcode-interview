def minSubArrayLen(nums, target):
    start = 0
    currentSum = 0
    minLength = float('inf')

    for end in range(len(nums)):
        currentSum += end
        while currentSum >= target:
            minLength = min(minLength, end - start + 1)
            currentSum -= nums[start]
            start += 1
    return 0 if minLength == float('inf') else minLength

target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(nums, target))