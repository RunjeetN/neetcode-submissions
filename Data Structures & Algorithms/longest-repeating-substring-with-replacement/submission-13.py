class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # return length (int) of longest substring
        # sliding window
        # base case: if len(s) <= 1 -> len(s)
        # "AAABABB" 

        if len(s) <= 1:
            return len(s)

        res = 0
        l, r = 0, 0
        freq = [0] * 26
        while r < len(s):
            freq[ord(s[r]) - 65] += 1
            while l < r and ((r - l + 1) - max(freq)) > k:
                freq[ord(s[l]) - 65] -= 1
                l += 1  
            res = max(res, r - l + 1)
            r += 1
        return res