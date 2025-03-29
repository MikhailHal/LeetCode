#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u',
                  'A', 'E', 'I', 'O', 'U']
        firstPtr = 0
        lastPtr = len(s) - 1
        ans = list(s)
        while True:
            while firstPtr < lastPtr:
                if not ans[firstPtr] in vowels:
                    firstPtr += 1
                else:
                    break
            while lastPtr > firstPtr:
                if not ans[lastPtr] in vowels:
                    lastPtr -= 1
                else:
                    break
            if firstPtr < lastPtr:
                tmp = ans[firstPtr]
                ans[firstPtr] = ans[lastPtr]
                ans[lastPtr] = tmp
                firstPtr += 1
                lastPtr -= 1
            else:
                break
        return "".join(ans)
        
# @lc code=end
