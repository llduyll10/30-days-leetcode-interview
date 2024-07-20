def twoSum(numbers, target):
    left, right = 0, len(numbers) -1

    while left < right:
        currentSum = numbers[left] + numbers[right]

        if currentSum == target:
            return [left+1, right+1]

        elif currentSum < target:
            left += 1 # Tăng con trỏ left lên để tăng tổng

        else:
            right -= 1 # Giảm con trỏ right xuống để giảm tổng
    return []


numbers = [2,7,11,15]
target = 9

print(twoSum(numbers, target))