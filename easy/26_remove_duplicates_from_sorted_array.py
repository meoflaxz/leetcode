# 26. Remove Duplicates from Sorted Array

# Given an integer array 'nums' sorted in non-decreasing order, remove the duplicates
# in-place such that each unique element appears only once. The relative order of the
# elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of 'nums' to be 'k', to get accepted,
# you need to do the following things:

# Change the array 'nums' such as that the first 'k' elements of nums contain the unique elements
# in the order they were present in 'nums' initially. The remaining elements of 'nums'
# are not important as well as the size of 'nums'

# Return 'k'.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # loop through list
        for element in nums:
            # check if there are item count more than 1
            if (nums.count(element) != 1):
                for index in range(0, nums.count(element) -1):
                    # delete that item based on the position
                    del(nums[nums.index(element)])

        return len(nums)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([1,1,2]))