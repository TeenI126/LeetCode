import Solutions.TwoSum

import random

import pytest
from hypothesis import given
from hypothesis.strategies import lists, integers

solution = Solutions.TwoSum.Solution()

@given(nums = lists(integers(min_value=-100000,max_value=100000),min_size=2, max_size=100))
def test_solution(nums):
    target = sum(random.sample(nums, 2))
    response = solution.twoSum(nums, target)

    assert sum([nums[i] for i in response]) == target
    pass

def test_manual_solution():
    nums = [1, 2, 34, 12354, 1245, 134, 5612, 354, 63, 526, 5, 7346, 5742, 367, 45, 7245, 62, 56, 24547, 235, 6235, 462345,
     762, 41, 514]
    target = sum(random.sample(nums, 2))
    response = solution.twoSum(nums, target)

    assert sum([nums[i] for i in response]) == target
    pass