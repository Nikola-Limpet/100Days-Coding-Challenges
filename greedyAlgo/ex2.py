# Money Chnage Problem:
""" 
  Given a non negative int money, find the minimum number of with denomination
  1,5,10 that changes money.
  Example:
  the minimum number of coins needed to change money = 26 is 6 = 10 + 10 + 5 + 1 + 1 + 1
"""

def change(money: int, domination : list ):
  if money == 0:
    return 0
  maxCoin = max(domination)
  return 1 + change(money - maxCoin, domination)
    

# Chage(8, [1,4,6]) ??

print(change(8, [1,4,6]))