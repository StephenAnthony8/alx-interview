#!/usr/bin/python3
""" 0-making_change """

def makeChange(coins=[], total=int):
    if (total <= 0) or (len(coins) < 1): 
        return 0
    
    # sort list
    coins.sort()
    coins.reverse()

    # loop 1 holds the initial loop
    for i in range(len(coins)):
        count = 0
        rem_total = total
        # inside loop holds the remaining values loop
        for j in range(i, len(coins)):
            while (coins[j] <= rem_total):
                rem_total -= coins[j]
                count += 1
                # if inside loop returns -1, loop 1 continues iterating till end
                if (rem_total == 0):
                    return(count)
    # if both loops return -1, exit function
    return (-1)    


print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))