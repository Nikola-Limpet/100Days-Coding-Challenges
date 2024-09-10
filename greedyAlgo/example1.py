# chose the largest number as posible 
# given an array of number and try to arraage the given to be as largest as possibe

numbers = [ 9, 8, 9 ,1 ,6]

# Greedy Algorithm 

largestNum = []

for i in range(len(numbers)):
    maxNum= max(numbers)
    largestNum.append(maxNum)
    numbers.remove(maxNum)

print(largestNum)

def largestConcatenate(numbers):
    result = ""
    while numbers:
        maxNumber = max(numbers)
        result += str(maxNumber)
        numbers.remove(maxNumber)
    return result

print(largestConcatenate([1,2,4,5]))



# if money == 0:
#     return 0
#   min_coins = float('inf')
#   for coin in denominations:
#     if money >= coin:
#       num_coins = 1 + change(money - coin, denominations)
#       min_coins = min(min_coins, num_coins)
#   return min_coins

# print(change(8, [1, 4, 7]))