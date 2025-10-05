#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
'''
1. optimal substructure
strs[i]と同じ文字の出現回数を持つ単語がすでにあるか
ある場合->追加
ない場合->新規

2.state
・出現回数を記録するマップ
・strs[i]の出現回数を記録するマップ


3.reccurence relation
if str in occurenceMap:
  occurenceMap[xx] += str
else:
  occurenceMap[xx] = str

strをソートして昇順に。O(1)
辞書に登録。

'''
from typing import List
class Solution:
    def __get_occurence_of_str(self, value: str) -> dict:
        result = {}
        value = sorted(value)
        for c in value:
            if not c in result:
                result[c] = 1
            else:
                result[c] += 1
        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        all_occurence = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in all_occurence:
                all_occurence[key].append(str)
            else:
                all_occurence[key] = [str]
        
        for key in all_occurence:
            ans.append(all_occurence[key])
        return ans

# @lc code=end

Solution().groupAnagrams(["ddddddddddg","dgggggggggg"])
# [["dgggggggggg"],["ddddddddddg"]]

Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# [["bat"],["nat","tan"],["ate","eat","tea"]]

Solution().groupAnagrams([""])
# [[""]]

Solution().groupAnagrams(["a"])
# [["a"]]