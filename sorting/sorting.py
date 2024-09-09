
data = [1,2,3,4,4,5,5,6,6,6,66,32,5,3,66,43,645,6432,233232,21,11,12]

# print(sorted(data, reverse=True))
print(sorted(data, key= lambda x: -x %2 == 0))

print(sorted((x  for x in data if x % 2== 0), reverse=True))
# print(sorted)
# import random
# n = 1000
# data = [ random.randint(1,n) for _ in range(n)]
# print(data)

