class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # return max AMOUNT of water

        # [1,2,2,5,4,7,2,2]
        i, j = 0, len(heights) - 1
        res = -1
        while i < j:
            width = j - i
            amt = min(heights[i], heights[j]) * width
            if amt > res:
                res = amt
            if heights[i] <= heights[j]:
                i+=1
            else:
                j -= 1
        return res 
            



