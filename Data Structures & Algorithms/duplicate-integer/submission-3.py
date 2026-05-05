class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_vals = {}
        for num in nums:
            if num in count_vals:
                return True
            else:
                count_vals[num] = 1
        return False
        