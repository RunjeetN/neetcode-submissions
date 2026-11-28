class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return T/F if chars of s1 are in s2 contiguously
        # both s1 and s2 are lowercase english chars

        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        for c in s1:
            freq1[ord(c) - 97] += 1
        
        freq2 = [0] * 26

        l, r = 0, 0
        while r < len(s2):
            if (r - l + 1) > len(s1):
                freq2[ord(s2[l]) - 97] -= 1
                l += 1
            freq2[ord(s2[r]) - 97] += 1 
            if freq1 == freq2:
                return True 
            r += 1 
        return False 
        
            

