from __future__ import annotations
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        zipped_nums = list(enumerate(nums))
        zipped_nums = sorted(zipped_nums, key= lambda num: num[1])

        pivot_1 = 0
        pivot_2 = len(zipped_nums) - 1

        while pivot_1 < pivot_2:
            if zipped_nums[pivot_1][1] + zipped_nums[pivot_2][1] == target:
                return [zipped_nums[pivot_1][0], zipped_nums[pivot_2][0]]
            elif zipped_nums[pivot_1][1] + zipped_nums[pivot_2][1] < target:
                pivot_1 += 1
            else:
                pivot_2 -= 1