#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t_map = {}
        t_to_s_map = {}
        for i in range(len(s)):
            if s[i] in s_to_t_map:
                if s_to_t_map[s[i]] != t[i]:
                    return False
            else:
                s_to_t_map[s[i]] = t[i]

            if t[i] in t_to_s_map:
                if t_to_s_map[t[i]] != s[i]:
                    return False
            else:
                t_to_s_map[t[i]] = s[i]
        return True

# @lc code=end

Solution().isIsomorphic(s = "egg", t = "add")
# true

Solution().isIsomorphic(s = "foo", t = "bar")
# false

Solution().isIsomorphic(s = "paper", t = "title")
# true

Solution().isIsomorphic(s = "a", t = "b")
# true