class Solution:
    def reverseString(self, s: List[str]) -> None:
        firstPtr = 0
        lastPtr = len(s) - 1
        while firstPtr < floor(len(s)/2):
            tmp = s[firstPtr]
            s[firstPtr] = s[lastPtr]
            s[lastPtr] = tmp
            firstPtr += 1
            lastPtr -= 1
