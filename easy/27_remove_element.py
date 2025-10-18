# 27. Remove Element

# Given an integer array 'nums' and an integer 'val', remove all occureneces of 'val'
# in 'nums' in=place. The order of the elements may be changed. Then return the number of the
# elements in 'nums' which are not equal to 'val'.

# Consider the number of elements in 'nums' which are not equal to 'val' be 'k', to get accepted, you need to do following things:
# Change the array 'nums' such that the first 'k' elements of 'nums' contain the elements
# which are not equal to 'val'. The remaining elements of 'nums' are not important as well the size of 'nums'.
# Return 'k'

# Goal -> Remove all occurrences of `val` from the array and return the new length.
# if val is 2, means remove all 2
# then count item that is not 2
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeElement([3,2,2,3], 2))