# Gives and integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:

      x = str(x)
      if x == x[::-1]:
          return True
      else:
          return False

## Test Case
# input -> 121, output -> True
# input -> -121, output -> False
# input -> 10, output -> False

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(12321))
