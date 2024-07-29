#Problem 13: Roman To integer
# Given an integer, convert it to a roman numeral. 
# Input is guaranteed to be within the range from 1 to 3999.
# Example:
# Input: "III"
# Output: 3
# Input: "IV"
# Output: 4


def romanToInt(s: str) -> int:
  res = 0
  map = {'I': 1, 'V':5, "X": 10, "L":50, "C": 100, "D": 500, "M":1000}
        
  s = s.replace("IV", "IIII").replace("IX", "VIIII")
  s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
  s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
  for i in s:
    res += map[i]
  return res
