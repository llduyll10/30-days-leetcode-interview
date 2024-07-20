def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n

    leftProduct = 1
    for i in range(n):
        output[i] = leftProduct
        leftProduct *= nums[i]
    rightProduct = 1
    for i in range(n-1, -1, -1):
        output[i] *= rightProduct
        rightProduct *= nums[i]
    return output