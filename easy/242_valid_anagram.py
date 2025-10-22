# 242. Valid Anagram

# Given 2 strings 's' and 't', return 'true' if t is an anagram of 's', and 'false' otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(t) == sorted(s):
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))