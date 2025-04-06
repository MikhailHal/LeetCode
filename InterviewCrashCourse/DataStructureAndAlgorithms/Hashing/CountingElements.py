from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        element_set = set(arr)
        count = 0
        for num in arr:
            if num + 1 in element_set:
                count += 1         
        return count
    
Solution().countElements([1,1,2])