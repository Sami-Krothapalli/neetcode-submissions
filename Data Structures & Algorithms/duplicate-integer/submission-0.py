class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        countNums = {}
        
        for num in nums:
            if num not in countNums:
                countNums[num] = 1
            else:
                countNums[num] += 1
        
        for num in countNums:
            if countNums[num] > 1:
                return True
        return False