# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

from functools import reduce
from operator import xor

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor bitwiser cancel itself when in pair, this way the only one that do not have pair will show up
        return reduce(xor,nums)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([1,2,3,2,3,1,10]))
    