# https://leetcode.com/problems/two-sum/
def twoSum(nums, target):
    hashMap = {} #to store numbers and their indices
    for i, num in enumerate(nums):
        # i will be the intex and num will be the number
        c = target - num
        # to find the complement
        if c in hashMap:
            return [hashMap[c],i]
            # Found a pair, return their indices
        hashMap[num] = i
        
nums = [1, 2, 3, 4]
target = 6
result = twoSum(nums, target)
print(result)
    