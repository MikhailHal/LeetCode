#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        left = right = 0
        if len(s1) > len(s2):
            return False
        
        for c in s1:
            if c in s1_dict:
                s1_dict[c] += 1
            else:
                s1_dict[c] = 1
        
        while right < len(s2):
            s2_dict = {}
            # 固定ウィンドウを作成
            if len(s2[left:right+1]) < len(s1):
                right += 1
                continue
            # ウィンドウ内の文字列を辞書へ落とし込んで出現回数をメモ
            for c in s2[left:right+1]:
                if c in s2_dict:
                    s2_dict[c] += 1
                else:
                    s2_dict[c] = 1
            if s1_dict == s2_dict:
                return True
            right += 1
            left += 1
        return False

# @lc code=end

print(Solution().checkInclusion("adc", "dcda"))
print(Solution().checkInclusion("ab", "eidbaoooo"))
print(Solution().checkInclusion("abo", "eidbaoooo"))
print(Solution().checkInclusion("ab", "eidboaoo"))
print(Solution().checkInclusion("a", "a"))
print(Solution().checkInclusion("a", "b"))
print(Solution().checkInclusion("aa", "b"))