class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return [i, j] 1 INDEXED
        # i < j
        # assumption: one valid solution

        i, j = 0, len(numbers) - 1

        while i < j:
            n1, n2 = numbers[i], numbers[j]
            if n1 + n2 < target:
                i += 1
            elif n1 + n2 > target:
                j -= 1
            else:
                return [i + 1, j + 1]
        return [-1, -1]
