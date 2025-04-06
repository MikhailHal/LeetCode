from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        plusOneDict = {}
        ans = 0
        for i in arr:
            if not i in plusOneDict:
                plusOneDict[i] = i+1
        
        for i in arr:
            if plusOneDict[i] in arr:
                ans += 1
        return ans
    
Solution().countElements([1,1,3,3,5,5,7,7])