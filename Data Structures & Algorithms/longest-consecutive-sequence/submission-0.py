class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        setNums = set(nums)
        current_length = 1
        longest = 1
        seen = set()

        for x in setNums:
             if x - 1 not in setNums:
                current_length = 1
                next_val = x + 1
                while next_val in setNums:
                    current_length += 1
                    next_val += 1
                longest = max(longest, current_length)
        
        return longest
