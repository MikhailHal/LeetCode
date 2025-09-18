#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for c in s:
            if not c in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] += 1

        for c in t:
            if not c in t_dict:
                t_dict[c] = 1
            else:
                t_dict[c] += 1
        
        return s_dict == t_dict
# @lc code=end

print(Solution().isAnagram("anagram", "anagram")) # true
print(Solution().isAnagram("rat", "car")) # false
print(Solution().isAnagram("a", "a")) # true
print(Solution().isAnagram("a", "b")) # false