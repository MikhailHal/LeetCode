from typing import List
import itertools

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefixSum = list(itertools.accumulate(nums))
        ans = [-1]*len(nums)
        for i in range(len(nums)):
            if i < k:
                continue
            if i+k >= len(nums):
                break
            if i-k <= 0:
                ans[i] = int(prefixSum[i+k] / (k*2+1))
            else:
                ans[i] = int((prefixSum[i+k] - prefixSum[i-k-1]) / (k*2+1))
        print(ans)
        return ans
              
Solution().getAverages([8],100000)
'''
indexed:    0,1,2,3 ,4 ,5
each value: 1,2,3,4 ,5 ,6
prefix sum: 1,3,6,10,15,21
'''

'''
・calculate prefix sum of nums
・process following steps until the end of nums
    ・check i's range(whether it meets k)
    ・calculate average of its subarray with prefix sum
    ・set the average value to list of ans
・return ans
'''