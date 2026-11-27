class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return LENGTH of longest substring
        # assumption: spaces count as valid chars or no spaces in input
        # input might have different cases -> normalize toLower

        seen = set()
        res = 0
        l, r = 0, 0
        while r < len(s):
            while s[r] in seen and l < r:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
            r += 1 
        return res

        




