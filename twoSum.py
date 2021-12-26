def twoSum( nums, target: int) :
    dic = dict()
    for i in range(len(nums)):
        dic[nums[i]] = i
    for i in range(len(nums)):
        if (target - nums[i]) in dic and i != dic[target - nums[i]]:
            return [i,dic[target - nums[i]]]
print(twoSum([3,2,4],6))