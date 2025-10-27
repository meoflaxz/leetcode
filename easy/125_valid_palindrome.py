# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string 's', return 'true' if it is palindrome, or 'false' otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

import re
pattern = r'[^A-Za-z0-9]'

class Solution:
    def isPalindrome(self, s:str) -> bool:

        result = re.sub(pattern, '', s).lower()
        return result == result[::-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(" "))