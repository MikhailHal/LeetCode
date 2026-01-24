#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
"""
・部分問題(本流)
    ・現ノードが陸かつ未訪問の場合カウント

・部分問題(dfs)
    ・現ノードが範囲外であれば終了
    ・現ノードが陸であれば訪問済みとしてマーク
    ・前後左右に対し走査開始

・例外
    ・上記部分問題を破壊するケースはなし

・状態
    ・島の数(int)
    ・訪問状態(List[List[bool]])

・状態遷移
    ・上方向dfs：dfs(row-1, column)
    ・下方向dfs：dfs(row+1, column)
    ・左方向dfs：dfs(row, column-1)
    ・右方向dfs：dfs(row, column+1)
"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_row = len(grid)
        max_column = len(grid[0])

        ans = 0
        seen: List[List[bool]] = [[False] * max_column for _ in range(max_row)]
        def __markIsland(row: int, column: int):
            if row < 0 or row >= max_row:
                return
            if column < 0 or column >= max_column:
                return
            if grid[row][column] != "1":
                return
            if seen[row][column]:
                return

            seen[row][column] = True
            __markIsland(row - 1, column)
            __markIsland(row + 1, column)
            __markIsland(row, column - 1)
            __markIsland(row, column + 1)
            return
        
        for row in range(max_row):
            for column in range(max_column):
                is_seen = seen[row][column]
                if grid[row][column] == "1" and not is_seen:
                    ans += 1
                    seen[row][column] = True
                    __markIsland(row - 1, column)
                    __markIsland(row + 1, column)
                    __markIsland(row, column - 1)
                    __markIsland(row, column + 1)
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