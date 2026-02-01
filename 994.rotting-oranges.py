#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from typing import List
from collections import deque
"""
・部分問題(準備)
    ・新鮮なオレンジの個数を計算

・部分問題(bfs)
    ・queueが空なら終了
    ・queueの中身のそれぞれに対して4方向腐らせる
    ・経過時間をカウント

・部分問題(rotting)
    ・上下左右それぞれに対して下記を実施
        ・当該マスが範囲内だったら腐らせる
        ・新たに腐った場合はqueue追加

・例外
    ・腐るものがない
    ・腐らないオレンジがあった

・状態
    ・新鮮なオレンジの数:int
    ・時点で新たに腐ったみかん:queue
    ・経過時間:int

・遷移
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_orange = 0
        ans = -1
        max_row = len(grid)
        max_column = len(grid[0])
        queue = deque()

        def __rotten(r: int, c: int):
            nonlocal max_row, max_column, queue, fresh_orange
            if r < 0 or r >= max_row or c < 0 or c >= max_column:
                return
            if grid[r][c] == 1:
                grid[r][c] = 2
                queue.append((r,c))
                fresh_orange -= 1
            return
        
        def __bfs():
            nonlocal queue, fresh_orange, ans

            while queue:
                queue_len = len(queue)
                for _ in range(queue_len):
                    (r,c) = queue.popleft()
                    __rotten(r - 1, c)
                    __rotten(r + 1, c)
                    __rotten(r, c - 1)
                    __rotten(r, c + 1)
                ans += 1
            
            if fresh_orange > 0:
                ans = -1
            return
        
        for r in range(max_row):
            for c in range(max_column):
                if grid[r][c] == 1:
                    fresh_orange += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        if len(queue) <= 0 and fresh_orange <= 0:
            return 0
        
        __bfs()
        return ans
        
# @lc code=end

print(Solution().orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))
# 4

print(Solution().orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))
# -1

print(Solution().orangesRotting(grid = [[0,2]]))
# 0

print(Solution().orangesRotting(grid = [[0]]))
# 0

print(Solution().orangesRotting(grid = [[1]]))
# -1