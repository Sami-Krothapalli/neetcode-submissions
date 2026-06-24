class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if num not in hashmap:
                diff = target - num
                hashmap[diff] = i
            else:
                return [hashmap[num], i]

        