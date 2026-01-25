#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
"""
・部分問題(メイン)
    ・全マスをループ
    ・各マスでdfsを呼び、面積の最大値を更新

・部分問題(dfs)
    目的：現在マスを含む島の面積を返却
    引数：行位置(r), 列位置(c)
    ・範囲外 or 水 or 訪問済み → 0を返す
    ・訪問済みとしてマーク
    ・自分(1) + 4方向のdfs結果を返す

・例外
    ・マスが1つのみ → dfs内で処理される
    ・値が1のマスがない → dfsが全て0を返す

・状態
    ・最高領域サイズ(max_area)：int
    ・巡回済みか否かの判定(seen)：List[List[bool]]

・状態遷移
    if 範囲外 or grid[r][c] != 1 or seen[r][c]:
        return 0
    seen[r][c] = True
    return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)
"""
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_r = len(grid)
        max_c = len(grid[0])
        max_area = 0
        seen = [[False] * max_c for _ in range(max_r)]

        def __calcCurrentArea(r: int, c: int) -> int:
            nonlocal max_c, max_r, seen

            if r < 0 or r >= max_r or c < 0 or c >= max_c:
                return 0
            if grid[r][c] != 1:
                return 0
            if seen[r][c] == True:
                return 0
            
            seen[r][c] = True
            return 1 + __calcCurrentArea(r-1, c) + __calcCurrentArea(r+1, c) + __calcCurrentArea(r, c-1) + __calcCurrentArea(r, c+1)
        
        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] == 1 and seen[r][c] == False:
                    max_area = max(__calcCurrentArea(r,c), max_area)
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