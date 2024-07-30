# Problem count unqiue char 

def countUniqueChars(s: str) -> int:
  
  return len(set(s)) == len(s)

# Test cases


print(countUniqueChars("abc")) # True
print(countUniqueChars("aabc")) # False

# Using hash lookup

def countUnqiueChar(s):
  if s is None:
    return False
  charSet = set()
  for i in s:
    if i in map:
      return False
    else:
      charSet.add(i)
  return True