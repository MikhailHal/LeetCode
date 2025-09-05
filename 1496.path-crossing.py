#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        point = [0,0]
        visited.add((point[0], point[1]))
        for direction in path:
            # 座標を移動
            if direction == 'N':
                point[1] += 1
            elif direction == 'S':
                point[1] -= 1
            elif direction == 'E':
                point[0] += 1
            elif direction == 'W':
                point[0] -= 1
            
            if (point[0], point[1]) in visited:
                return True
            else:
                visited.add((point[0], point[1]))
        return False

        
# @lc code=end

print(Solution().isPathCrossing("NESW"))