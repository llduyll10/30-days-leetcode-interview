def removeDuplicate(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k

nums = [ 0,0,1,1,1,2,2,3,3,4 ]

print(removeDuplicate(nums))