class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] + nums[i] == target and j != i:
                    if j < i:
                        return [j , i]
                    else:
                        return [i, j]