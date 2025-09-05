#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start
from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityMap = {}
        # 各pathの0番目の要素をキー・1番目の要素をバリューとして格納
        # 各pathの1番目の要素をキーとして格納。バリューは空文字
        for path in paths:
            depature = path[0]
            arrive = path[1]
            cityMap[depature] = arrive
            if not arrive in cityMap:
                cityMap[arrive] = ""
        for key in cityMap:
            if cityMap[key] == "":
                return key
        # バリューの中身がからのものが答え
# @lc code=end

print(Solution().destCity([["London","New York"]]))