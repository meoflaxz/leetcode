# Given a string 's' containing just the characters '(', ')', '{', '}', '[', ']', determine if the input string is valid.

# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false

class Solution:
  def isValid(self, s: str) -> bool:

    parentheses_dict = {
                      'Parentheses': ['(', ')'],
                      'square': ['[',']'],
                      'curly': ['{','}']
    }

    changed = True
    while changed:
        changed = False
        ## positionized input of s
        for i in range(len(s) - 1):
          char1 = s[i]
          char2 = s[i + 1]

          ## positionized item for bracket to compare with s later on
          for key in parentheses_dict:
            open_bracket = parentheses_dict[key][0]
            close_bracket = parentheses_dict[key][1]

            if char1 == open_bracket and char2 == close_bracket:
                s = s[:i] + s[i+2:]
                changed = True
                break

          if changed:
            break
    return s == ''


if __name__ == "__main__":

  solution = Solution()
  print(solution.isValid('()())'))
