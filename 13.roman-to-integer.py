#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        skip = False
        roman_map = {
            "I" : 1,
            "IV" : 4,
            "IX" : 9,
            "V" : 5,
            "X" : 10,
            "XL" : 40,
            "XC" : 90,
            "L" : 50,
            "C" : 100,
            "CD" : 400,
            "CM" : 900,
            "D" : 500,
            "M" : 1000
        }

        for i, c in enumerate(s):
            # 前回特殊ケースを処理した場合今回はスキップ
            if skip:
                skip = False
                continue
            # 今回の数字がIVなど特殊ケースの場合
            if i+1 < len(s) and ''.join(s[i] + s[i+1]) in roman_map:
                sum += roman_map[''.join(s[i] + s[i+1])]
                skip = True
                continue
            sum += roman_map[c]
        return sum

        
# @lc code=end

print(str(Solution().romanToInt(s = "MCMXCIV")))
# 1994

print(str(Solution().romanToInt(s = "III")))
# 3

print(str(Solution().romanToInt(s = "LVIII")))
# 58

print(str(Solution().romanToInt(s = "M")))
# 1000