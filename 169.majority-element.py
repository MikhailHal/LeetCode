#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
"""
・numsに対して下記の操作を開始
    ・numをキーとしてハッシュマップに保存。バリューは出現回数
・ハッシュマップに対して下記の操作を開始
    ・ハッシュマップの値内で最大値を取る
"""
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mostAppearedNum = 0
        ans = 0
        hashmap = dict()
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for _, key in enumerate(hashmap):
            if hashmap[key] > mostAppearedNum:
                mostAppearedNum = max(mostAppearedNum, hashmap[key])
                ans = key
        print(ans)
        return ans
        
# @lc code=end
Solution().majorityElement([2,2,1,1,1,2,2])
