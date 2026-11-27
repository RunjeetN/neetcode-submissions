class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if len nums < 0: []
        # if no nums sum to 0 : []
        # return: [[i, j, k]]
        res = []
        if len(nums) < 3:
            return res 
       

        nums.sort()
        seen = set()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r :
                summ = n + nums[l] + nums[r]

                if summ > 0:
                    r -= 1
                elif summ < 0:
                    l += 1 
                else: 
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            seen.add(n)
        return res 
                
        

