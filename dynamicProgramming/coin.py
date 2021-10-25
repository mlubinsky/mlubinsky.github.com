# https://runestone.academy/runestone/books/published/pythonds/Recursion/DynamicProgramming.html
# making change using the fewest coins

# following algo is innefficient bevause of recursion
def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins


print(recMC([1,5,10,25],63))

# dpMakeChange takes three parameters: 
# 1. list of valid coin values, 
# 2. amount of change we want to make, 
# 3. list of the minimum number of coins needed to make each value.

def dpMakeChange(coinValueList,change,minCoins):
   for cents in range(change+1):
      coinCount = cents
      
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
              
      minCoins[cents] = coinCount
      
   return minCoins[change]

# Code above  allows figuring out the minimum number of coins, 
# it does not help us make change since we do not keep track of the coins we use. 
# We can easily extend dpMakeChange to keep track of the coins used by simply remembering the last coin we add for each entry in the minCoins table. 
# If we know the last coin added, 
# we can simply subtract the value of the coin to find a previous entry in the table that tells us the last coin we added to make that amount. 
# We can keep tracing back through the table until we get to the beginning.

#  This shows the algorithm in action solving the problem for our friends in Lower Elbonia. 
# The first two lines of main set the amount to be converted and create the list of coins used. 
# The next two lines create the lists we need to store the results. coinsUsed is a list of the coins used to make change, 
# and coinCount is the minimum number of coins used to make change for the amount corresponding to the position in the list.

# Notice that the coins we print out come directly from the coinsUsed array. 


def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()

