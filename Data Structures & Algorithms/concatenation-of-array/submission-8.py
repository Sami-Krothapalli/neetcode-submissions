class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for m in range(2):
            for num in nums:
                ans.append(num)
        return ans

        