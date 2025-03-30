from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = 0.0
        sum = 0
        left = 1
        for right in range(k):
            sum += nums[right]
        ans = sum / k
        while left + k - 1 < len(nums):
            right = left + k - 1
            sum -= nums[left - 1]
            sum += nums[right]
            ans = max(ans, sum/k)
            left += 1
        return ans
    