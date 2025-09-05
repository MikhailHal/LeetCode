#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start
from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dep = set()
        des = set()
        for path in paths:
            dep.add(path[0])
            des.add(path[1])
        return (des - dep).pop()
# @lc code=end

print(Solution().destCity([["London","New York"]]))