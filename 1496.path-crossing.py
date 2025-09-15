#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos_visit = set()
        pos_visit.add((0, 0))
        x = y = 0
        for unit in path:
            if unit == 'N':
                y += 1
            elif unit == 'S':
                y -= 1
            elif unit == 'E':
                x += 1
            else:
                x -= 1
            if (x, y) in pos_visit:
                return True
            pos_visit.add((x, y))
        return False

        
# @lc code=end
print(Solution().isPathCrossing("NES")) # false
print(Solution().isPathCrossing("NESW")) # true
print(Solution().isPathCrossing("N")) # false