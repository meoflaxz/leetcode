# 231. Power of Two

# Given an integer n, return true if it is a power or two.
# Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n==2x

import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # check both condition
        # first condition, n must be greater than 0 (which is true for integer of power of two)
        # second condition, equation of n shouldnt be 0
        # power of two will always have one distinct 0 in bits
        # comparing the n & n-1 through bitwise operation, result should always to 0
        # this just means that the code is looking n that is greater than 0 and checking True for second condition
        return n > 0 and not (n & (n -1))
        # can also be written as (n & (n-1)) == 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPowerOfTwo(2))