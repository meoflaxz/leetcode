# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with '0(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if target == num:
                return  i
            # first encounter of bigger num means it should be inserted here
            if num > target:
                return i
            
        # if target too big means it will be inserted at the index+1 position
        return len(nums)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1,2,3], 5))