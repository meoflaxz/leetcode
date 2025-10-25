# 415. Add Strings

# Given 2 non-negative integers, 'num1' and 'num2' represented as string, return the sum of 'num1' and 'num2' as a string.

# You must solve the problem without using any built-in library for handling large integers (such as 'BigInteger').
# You must also not convert the inputs to integers directly.

# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"

# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"

import sys

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # set maximum limit for int to str conversion
        # if not, will got error
        sys.set_int_max_str_digits(10000)
        return str(int(num1) + int(num2))
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.addStrings(123,123))