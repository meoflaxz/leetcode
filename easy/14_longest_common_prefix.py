# 14. Longest Common Prefix

## Write a function to find the longest common prefix string amongst an array of strings.
## If there is no common prefix, return an empty string "".

## Example 1
## Input: strs = ["flower", "flow", "flight"]
## Output: "fl"

## Example 2
## Input: strs = ["dog", "racecar", "car"]
## Output: ""
## Explanation: There is no common prefix among the input strings.


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ## if list is empty
        if not strs:
            return ""

        prefix = strs[0]

        ## compare each string in list with first prefix
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                ## if when we remove last character, then nothing left, it means it is not a list, and no common prefix
                if not prefix:
                    return ""
        return prefix

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["car","racecar"]))
