class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count_Map = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff not in count_Map:
                count_Map[num] = idx
            else:
                return [count_Map[diff], idx]