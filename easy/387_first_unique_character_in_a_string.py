# 387. First Unique Character in a String

# Given a string 's', find the first non-repeating character in it and return its index.
# If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:

        # create dictionary to store char count
        char_count = {}

        # loop throughout string, plus 1 to value if key already exists
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # find the only one that not repeated
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        # if all is duplicate, return -1, following question
        return -1
    
solution = Solution()
print(solution.firstUniqChar("KKK"))