from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        fliped = 0
        ans = 0
        curr = 0

        for right in range(len(nums)):
            curr += 1
            if nums[right] == 0:
                fliped += 1
            while fliped > k:
                if nums[left] == 0:
                    fliped -= 1
                curr -= 1
                left += 1
            ans = max(ans, curr)
        return ans 


Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)