# 66. Plus One

# You are given a large integer represented as an integer array digits, where each digits[i] is the
# ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading '0's/
# Increment the large integer by one and return the resulting array of digits.

from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    num = int(''.join(map(str, digits)))
    num += 1
    num = list(int(d) for d in str(num))
    return num

if __name__ == "__main__":
  solution = Solution()
  print(solution.plusOne([2,3,4]))
