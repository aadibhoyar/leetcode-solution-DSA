### 1. [Two Sum](https://leetcode.com/problems/two-sum/) 🟩
###### Time Complexity: O(n^2) Date: 25.09.2024  
```Java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++){
            for (int j = i + 1 ; j < nums.length; j++){
                if (nums[i] + nums[j] == target){
                    return new int[]{i,j};
                }
            }
        }
        return nums;
    }
}
```

### 242. [Valid Anagram](https://leetcode.com/problems/valid-anagram/) 🟩
###### Time Complexity: O(n log n) Date: 27.09.2024  
```Java
class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        Arrays.sort(sArray);
        Arrays.sort(tArray);
        return Arrays.equals(sArray, tArray);
    }
}
```

### 217. [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) 🟩
###### Time Complexity: O(n log n) Date: 27.09.2024  
```Java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;  // duplicate found
            }
        }

        return false; // no duplicate
    }
}
```

### 49. [Group Anagrams](https://leetcode.com/problems/group-anagrams/description/) 🟨
###### Time Complexity: O(n * k log k) Date: 29.09.2024  
```Java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedStr = new String(charArray);
    
            if (!map.containsKey(sortedStr)) {
                map.put(sortedStr, new ArrayList<>());
            }
            map.get(sortedStr).add(str);
        }
        return new ArrayList<>(map.values());
    }
}

```


