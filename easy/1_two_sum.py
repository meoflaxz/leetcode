# Given an array of integers nums and an interget target, return indices of the two numbers such that they
# add up to target.

# You may assume that each inpyt would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # convert List to readable integer for arithmetic operations

    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
          return [i, j]

# Test case and input
# Test case 1 -> nums = [2,7,11,15], target = 9, output = [0,1]
# Test case 2 -> nums = [3,2,4], target = 6, output = [1,2]
# Test case 3 -> nums = [3,3], target = 6, output = [0,1]

if __name__ == "__main__":
  solution = Solution()

  nums   = [2,7,11,15]
  target = 9

  nums1  = [2,7,11,15]
  target2 = 9

  nums2 = [3,2,4]
  target2 = 6

  nums3 = [3,3]
  target3 = 6

  print(solution.twoSum(nums, target))


