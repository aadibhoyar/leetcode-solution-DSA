# https://leetcode.com/problems/valid-anagram/

def isAnagram(s,t):
        s = sorted(s)
        t = sorted(t)
        if s == t:
                return True
        return False

# Example usage:
s = "rat"
t = "car"
print(isAnagram(s,t))
