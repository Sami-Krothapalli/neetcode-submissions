class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_Count = {}
        for num in nums:
            if num not in num_Count:
                num_Count[num] = 1
            else:
                return True
        return False
