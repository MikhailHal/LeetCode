#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split(" ")
        pattern_to_s = {}
        s_to_pattern = {}

        if len(pattern) != len(word_list):
            return False
        
        for i, pat in enumerate(pattern):
            if not pat in pattern_to_s:
                pattern_to_s[pat] = word_list[i]
            else:
                if pattern_to_s[pat] != word_list[i]:
                    return False
        
        for i, word in enumerate(word_list):
            if not word in s_to_pattern:
                s_to_pattern[word] = pattern[i]
            else:
                if s_to_pattern[word] != pattern[i]:
                    return False
        return True


# @lc code=end

Solution().wordPattern(pattern = "abba", s = "dog cat cat dog")
# true

Solution().wordPattern(pattern = "abba", s = "dog cat cat fish")
# false

Solution().wordPattern(pattern = "aaaa", s = "dog cat cat dog")
# false