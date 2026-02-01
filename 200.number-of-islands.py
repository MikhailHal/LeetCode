#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
"""
・部分問題(main)
    目的：(0,0)~(r_max,c_max)まで走査し時点での島数を数える
    引数：-
    ・(0,0)から最後まで探索開始
    ・現座標が1かつ未訪問であればdfs開始
    ・ansカウント
・部分問題(dfs)
    目的：(r,c)自身から派生する陸を走査
    引数：座標(r,c)
    ・現座標が範囲外だったらスキップ
    ・現座標が0だったらスキップ
    ・現座標が訪問済みだったらスキップ
    ・現座標を訪問済みにする
    ・上下左右に同dfs処理を呼ぶ

・例外
    部分問題を破壊する例外はない

・状態
    ・訪問状態：visited[List[bool]]
    ・島数：ans int

・遷移
    if 範囲外:
        return
    if grid[r][c]が水(==0):
        return
    if visited[r][c]が訪問済み:
        return
    __dfs(r - 1, c)
    __dfs(r + 1, c)
    __dfs(r, c - 1)
    __dfs(r, c + 1)

"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_row, max_column = len(grid), len(grid[0])
        ans = 0
        visited = [[False] * max_column for _ in range(max_row)]
        def __dfs(r: int, c: int):
            nonlocal max_row, max_column, visited
            if r < 0 or r >= max_row or c < 0 or c >= max_column:
                return
            if grid[r][c] == "0" or visited[r][c] == True:
                return
            
            visited[r][c] = True
            __dfs(r - 1, c)
            __dfs(r + 1, c)
            __dfs(r, c - 1)
            __dfs(r, c + 1)
            return
        for r in range(max_row):
            for c in range(max_column):
                if grid[r][c] == "1" and visited[r][c] == False:
                    __dfs(r,c)
                    ans += 1
        return ans
        
# @lc code=end

print(Solution().numIslands(
    grid =
    [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
)) # 1

print(Solution().numIslands(
    grid =
    [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
)) # 3