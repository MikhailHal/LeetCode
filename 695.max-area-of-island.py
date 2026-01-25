#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
"""
・部分問題(メイン)
    ・g(0,0)から値が1のマスのみ走査開始
    ・当該マスが巡回済みの場合はスキップ
    ・4方向にdfsを行い1の数をカウント
・部分問題(dfs)
    目的：当該領域時点における領域サイズを返却
    引数：行位置(r), 列位置(c), 現在の領域(curr_area)
    ・curr_celが範囲外or走査済みor1以外の場合は終了
    ・curr_areaをインクリメント
    ・走査済みとしてマーク
    ・4方向にdfs実施

・例外
    ・マスが1つのみ
    ・値が1のマスがない

・状態
    ・最高領域サイズ(max_area)：int
    ・現時点での領域サイズ(curr_area)：int
    ・巡回済みか否かの判定(seen)：List[List[bool]]

・状態遷移
    if seen[r][c] == True or 範囲外:
        return curr_area
    curr_area += 1
    seen[r][c] = True
    curr_area = dfs(grid[r-1][c], curr_area)
    curr_area = dfs(grid[r+1][c], curr_area)
    curr_area = dfs(grid[r][c-1], curr_area)
    curr_area = dfs(grid[r][c+1], curr_area)
    return curr_area
"""
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_r = len(grid)
        max_c = len(grid[0])
        max_area = 0
        seen = [[False] * max_c for _ in range(max_r)]

        def __calcCurrentArea(r: int, c: int, curr_area: int) -> int:
            nonlocal max_c, max_r, seen

            if r < 0 or r >= max_r or c < 0 or c >= max_c:
                return curr_area
            if grid[r][c] != 1:
                return curr_area
            if seen[r][c] == True:
                return curr_area
            
            curr_area += 1
            seen[r][c] = True
            curr_area = __calcCurrentArea(r-1, c, curr_area)
            curr_area = __calcCurrentArea(r+1, c, curr_area)
            curr_area = __calcCurrentArea(r, c-1, curr_area)
            curr_area = __calcCurrentArea(r, c+1, curr_area)
            return curr_area
        
        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] == 1 and seen[r][c] == False:
                    curr_area = 1
                    seen[r][c] = True
                    curr_area = __calcCurrentArea(r-1, c, curr_area)
                    curr_area = __calcCurrentArea(r+1, c, curr_area)
                    curr_area = __calcCurrentArea(r, c-1, curr_area)
                    curr_area = __calcCurrentArea(r, c+1, curr_area)
                    max_area = max(max_area, curr_area)
        return max_area
                    
        
# @lc code=end

print(Solution().maxAreaOfIsland(
    grid = 
    [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ])
) #6

print(Solution().maxAreaOfIsland([[0,0,0,0,0,0,0,0]])) #0
print(Solution().maxAreaOfIsland([[0]])) #0
print(Solution().maxAreaOfIsland([[1]])) #1