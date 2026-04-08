class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h_map = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in h_map:
                return [h_map[complement], i]

            h_map[num] = i