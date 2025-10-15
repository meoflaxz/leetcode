# 500. Keyboard Roww

# Given an array of string words, return the words that can be typed using letters of the alphabet on only
# one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.
# In the American keyboard:
# the first row consists of the characters "qwertyuiop".
# the second row consists of the characters "asdfghjkl"
# the third row consists of the characters "zxcvbnm".

from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        row = {
                        "first": ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
                        "second": ["a","s","d","f","g","h","j","k","l"],
                        "third": ["z","x","c","v","b","n","m"]

                     }
        result = []

        # for i in row.values():
        #     for word in words:
        #         if all(char.lower() in i for char in word):

        #             # same with 
        #             # for char in word:
        #             #       char.lower() in i
        #             result.append(word)


        for word in words:
            for char in word:
                for i in char:
                    for j in i:
                        print(j)
        return result
if __name__ == "__main__":
    solution = Solution()
    print(solution.findWords(["ASD"]))