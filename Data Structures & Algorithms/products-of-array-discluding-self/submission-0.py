class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newList = [0] * len(nums)
        for i, x in enumerate(nums):
            newList[i] = math.prod(nums[:i] + nums[i+1:])
        return newList