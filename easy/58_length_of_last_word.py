# 58. Length of Last Word

# Given a string 's' consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    return len(s.split()[-1])


if __name__ == "__main__":
  solution = Solution()
  print(solution.lengthOfLastWord("SAYAMsAKAN"))
