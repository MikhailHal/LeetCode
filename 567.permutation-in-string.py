#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        right = left = 0
        s1_freq_dict = {}
        s2_freq_dict = {}

        # s1のほうが長い場合は解は存在しないため終了
        if len(s1) > len(s2):
            return False
        
        # s1の文字列内の各文字の出現回数を記録
        for c in s1:
            if c in s1_freq_dict:
                s1_freq_dict[c] += 1
            else:
                s1_freq_dict[c] = 1

        while right < len(s2):
            # 初期ウィンドウ構築
            while right < len(s1):
                if s2[right] in s2_freq_dict:
                    s2_freq_dict[s2[right]] += 1
                else:
                    s2_freq_dict[s2[right]] = 1
                right += 1
            
            # 出現回数が全て一致していたらpermutation出現
            if s1_freq_dict == s2_freq_dict:
                return True
            # rightインデックスが既にs2超えていたら終了
            if right >= len(s2):
                return False
            # ウィンドウをスライドしていく
            s2_freq_dict[s2[left]] -= 1
            if s2_freq_dict[s2[left]] == 0:
                s2_freq_dict.pop(s2[left])
            left += 1
            if s2[right] in s2_freq_dict:
                s2_freq_dict[s2[right]] += 1
            else:
                s2_freq_dict[s2[right]] = 1
            right += 1
        return s1_freq_dict == s2_freq_dict

# @lc code=end

print(Solution().checkInclusion("adc", "dcda"))
print(Solution().checkInclusion("ab", "eidbaoooo"))
print(Solution().checkInclusion("abo", "eidbaoooo"))
print(Solution().checkInclusion("ab", "eidboaoo"))
print(Solution().checkInclusion("a", "a"))
print(Solution().checkInclusion("a", "b"))
print(Solution().checkInclusion("aa", "b"))