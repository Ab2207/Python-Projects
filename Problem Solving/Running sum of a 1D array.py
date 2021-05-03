def runningSum(nums):

    res = []
    for i in range(len(nums)):
        if i == 0:
            res.append(nums[i])
        elif i > 0:
            nums[i] = nums[i] + nums[i - 1]
            res.append(nums[i])
    return res

print(runningSum([1,2,3,4]))