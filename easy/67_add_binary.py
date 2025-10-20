# 67. Add Binary

# Given 2 binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # input is in string, need to convert to integer for addition
        # convert to binary base 2
        int_a, int_b = int(a, 2), int(b, 2)

        sum = int_a + int_b

        # [2:] to remove 0b prefix in front
        return bin(sum)[2:]


if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary("11","1"))