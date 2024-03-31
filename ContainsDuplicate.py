# https://leetcode.com/problems/contains-duplicate

def cd(nums):
        s_num =  sorted(nums)
        for i in range(len(s_num) - 1):
            if s_num[i] == s_num[i + 1]:
                return True
    
        return False


# Example usage:
nums = [1,1,1,3,3,4,3,2,4,2]
print(cd(nums))  
