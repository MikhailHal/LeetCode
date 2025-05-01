from typing import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        playersResult = dict()
        ans = list(list())
        ans.append([])
        ans.append([])

        # initialize map and add all players as key
        for match in matches:
            playersResult[match[0]] = 0
            playersResult[match[1]] = 0
        
        # count losers
        for match in matches:
            playersResult[match[1]] += 1

        # extract players as answer who meet problem's requirements
        for player in playersResult:
            neverLost = playersResult[player] == 0
            oneLost = playersResult[player] == 1
            if neverLost:
                ans[0].append(player)
            if oneLost:
                ans[1].append(player)

        # sort results
        ans[0].sort()
        ans[1].sort()
        return ans
        
print(Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))