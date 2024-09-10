# Money Chnage Problem:
""" 
  Given a non negative int money, find the minimum number of with denomination
  1,5,10 that changes money.
  Example:
  the minimum number of coins needed to change money = 26 is 6 = 10 + 10 + 5 + 1 + 1 + 1
"""

# def change(money: int, denominations: list) -> int:
#   if money == 0:
#     return 0
#   minCoin  = float('inf')
#   for coin in denominations:
#     if  money >= coin:
#       numCoin =  1 + change(money- coin, denominations)
#       minCoin = min(numCoin, minCoin)
#   return minCoin


def newChange(money, denominations):
  count = 0
  while money > 0:
    largest = max(denominations)
    if money >= largest:
      money -= largest
      count += 1
    else:
      denominations.remove(largest)
  return count


print (newChange(8, [1,2,8])) 
# #coint= 2