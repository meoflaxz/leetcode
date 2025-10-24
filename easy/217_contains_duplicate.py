# 217. Contains Duplicate

# Given an integer array 'nums', return 'true' if any value appears at least twice in the array, return 'false' if
# every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation: The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # create set to hold distinct value
        value = set()

        for num in nums:
            if num in value:
                return True
            # store distinct value if not seen before, set will only store unique item
            value.add(num)


        # will return False if no unique value in list
        return False

solution = Solution()
print(solution.containsDuplicate([4,5,6,7,8,9,4]))


# ALTERNATIVE ANSWER
# return len(set(nums))<len(nums) -> SORT AND DEDUP ELEMENTS AUTOMATICALLY