class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        self.nums = nums
        self.target = target
        for i in range(len(self.nums)):
            if i < len(self.nums):
                if self.nums[i] + self.nums[i+1] == target:
                    return [i,i+1]
            