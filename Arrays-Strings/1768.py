# Problem: 1768. Merge Strings Alternately

# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. I
# if a string is longer than the other, 
# append the additional letters onto the end of the merged string.


# My solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def mergeAlternately(word1, word2):
  res = ""
  for i in range(min(len(word1), len(word2))):  
     # iterate through the length of the smallest string
    res += word1[i] + word2[i]
  return res + word1[i+1:] + word2[i+1:]  # append the remaining characters of the longest string

# Test Cases

print(mergeAlternately("abc", "pqr")) # "apbqcr"
print(mergeAlternately("ab", "pqrs")) # "apbqrs"
print(mergeAlternately("abcd", "pq")) # "apbqcd"
print(mergeAlternately("ab", "pqr")) # "apbqr"
print(mergeAlternately("a", "pqr")) # "apqr"
