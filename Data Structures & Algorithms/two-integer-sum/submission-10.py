class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if num not in hashmap:
                hashmap[diff] = i
            else:
                return [hashmap[num], i]

                
        