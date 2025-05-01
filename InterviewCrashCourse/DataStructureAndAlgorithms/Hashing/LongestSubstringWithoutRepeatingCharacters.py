class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # handle non-expected case
        if s == "":
            return 0
        
        appearsSet = set(s[0])
        ans = 1
        left, right = 0, 1

        # find substrings
        for right in range(1, len(s)):
            # check if new subwindow contains a duplicate character
            if s[right] in appearsSet:
                # if it's true, move to right left pointer until don't meet above conditions
                if s[left] == s[right]:
                    appearsSet.remove(s[left])
                    left += 1
                else:
                    while s[left] != s[right]:
                        appearsSet.remove(s[left])
                        left += 1
                    left += 1
            length = right - left + 1
            ans = max(ans, length)
            # add the character to the set
            appearsSet.add(s[right])
        
        return ans
        

print(Solution().lengthOfLongestSubstring("tmmzuxt"))