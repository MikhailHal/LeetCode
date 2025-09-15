#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start
from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        set_a = set()
        set_b = set()
        for path in paths:
            set_a.add(path[0])
            set_b.add(path[1])
        return ''.join(set_b - set_a)
# @lc code=end

print(Solution().destCity([["London","New York"]]))
print(Solution().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))