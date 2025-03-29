#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        """
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
        """
        vowels = set('aeiouAEIOU')
        list_s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not list_s[left] in vowels:
                left += 1
            while right > left and not list_s[right] in vowels:
                right -= 1
            if left < right:
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left += 1
                right -= 1
        return "".join(list_s)
        
# @lc code=end
