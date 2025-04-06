class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dict = {chr(ord('a') + i): 0 for i in range(26)}
        for c in sentence:
            dict[c] = dict[c] + 1
        
        for v in dict.values():
            if v == 0:
                return False
        return True
    
print(Solution().checkIfPangram("leetcode"))