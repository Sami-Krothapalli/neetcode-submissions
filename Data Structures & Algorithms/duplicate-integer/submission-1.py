class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isdupl = set()

        for i in range(len(nums)):
            if nums[i] in isdupl:
                return True
            else:
                isdupl.add(nums[i])

        return False
         