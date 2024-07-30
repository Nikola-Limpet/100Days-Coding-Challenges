def frequenceCount(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return freq


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(frequenceCount(arr))


def frequencesCount(filename):
  freq = {}
  for pieces in open(filename).read().lower().split():
      word = "".join(c for c in pieces if c.isalnum())
      if word:
          freq[word] = 1 + freq.get(word, 0)
  return freq
