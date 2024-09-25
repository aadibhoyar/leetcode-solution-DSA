### 1.[ Two Sum](https://leetcode.com/problems/two-sum/) 🟩
###### 25.09.2024
```python
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
twoSum(nums, target)
print(twoSum)
```
