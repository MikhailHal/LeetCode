#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0,0) : 1}
        point = [0,0]
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
            
            # 現在の位置を記録
            tupled = (point[0], point[1])
            if not tupled in visited:
                visited[tupled] = 1
            else:
                visited[tupled] += 1
            
            # 交差した箇所があるかどうか確認
            if visited[tupled] >= 2:
                return True
        return False

        
# @lc code=end

print(Solution().isPathCrossing("NES"))