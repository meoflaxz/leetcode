# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:

      s = s.upper()
      rom_dict = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000
                  }
# if smaller value comes before larger value, subtract it
      total = 0
      for i in range(len(s)):
        if i + 1 < len(s) and  rom_dict[s[i]] < rom_dict[s[i+1]]:
          total -= rom_dict[s[i]]
        else:
          total += rom_dict[s[i]]
      return total

      # return sum(map(rom_dict.get, s))

if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("Xi"))
