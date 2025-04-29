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
"""
Boyer-Moore majority vote algorithm
・numsに対して下記の操作を開始
    ・初期化(i=0)
        ・先頭の要素を過半数候補として使用
        ・カウンターを1にする
    ・nums[i]が過半数候補数字であればカウンターを増やす
    ・異なる場合は減らす
    ・操作した結果0だったらその時の数字を利用
"""
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
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
        """
        majorityElement = 0
        counter = 0
        for i, num in enumerate(nums):
            # 初期化処理
            if i == 0:
                majorityElement = num
                counter += 1
                continue
            
            # カウンター操作
            if majorityElement != num:
                counter -= 1
            else:
                counter += 1
            
            # カウンターの値を判断して過半数候補を確認
            if counter <= 0:
                counter = 1
                majorityElement = num
        print(majorityElement)
        return majorityElement
        
# @lc code=end
Solution().majorityElement([3,2,3])
