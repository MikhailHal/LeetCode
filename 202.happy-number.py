#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    """
    各桁の二乗和を算出

    :param int n 二乗和を計算する数値
    :return int 二乗和の計算結果
    """
    def __calc_pow_sum(self, n: int) -> int:
        sum = 0
        for c in str(n):
            sum += int(c) ** 2
        return sum

    def isHappy(self, n: int) -> bool:
        sum = 0
        is_occured = set()
        while True:
            sum = self.__calc_pow_sum(n)
            n = sum
            if n in is_occured:
                return False
            else:
                is_occured.add(n)

            if n == 1:
                return True

# @lc code=end

print("exp: True" + " / " + "act:" + str(Solution().isHappy(1)))
print("exp: True" + " / " + "act:" + str(Solution().isHappy(19)))
print("exp: False" + " / " + "act:" + str(Solution().isHappy(2)))
print("exp: True" + " / " + "act:" + str(Solution().isHappy(7)))