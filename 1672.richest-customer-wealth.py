#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richestAccount = 0
        for customer in accounts:
            currentAccount = 0
            for bank in customer:
                currentAccount = currentAccount + bank
            if(richestAccount < currentAccount):
                richestAccount = currentAccount
        return richestAccount
        
# @lc code=end
