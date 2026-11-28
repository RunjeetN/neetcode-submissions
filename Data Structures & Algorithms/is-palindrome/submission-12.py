class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        nums = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        
        normalized = ""
        for c in s:
            if c.isalpha() or c in nums:
                normalized += c

        return normalized == normalized[::-1]