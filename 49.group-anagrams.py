#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        ans = []
        for word in strs:
            key = ''.join(sorted(word))
            if not key in anagram_map:
                anagram_map[key] = [word]
            else:
                anagram_map[key].append(word)
        for key in anagram_map:
            ans.append(anagram_map[key])
        return ans

# @lc code=end

Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# [["bat"],["nat","tan"],["ate","eat","tea"]]

Solution().groupAnagrams([""])
# [[""]]

Solution().groupAnagrams(["a"])
# [["a"]]