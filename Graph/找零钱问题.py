def recMc(coinValueList,change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in coinValueList:
            if i < change:
                numCoins = 1 + recMc(coinValueList,change-i)
                if numCoins < minCoins:
                    minCoins = numCoins
    return minCoins

#假设63
#优化之后得代码（添加了查询表):
def recDc(coinValueList,change,knowList):
    minCoins =change
    if change in coinValueList:
        knowList[change] = 1
        return 1
    elif knowList[change] > 0:
        return knowList[change]
    else:
        for i in coinValueList:
            if i <= change:
                numCoins = 1 + recDc(coinValueList,change-i,knowList)
                if numCoins < minCoins:
                    minCoins = numCoins
                    knowList[change] = minCoins
    return numCoins
# print(recDc([1,5,10,25],26,[0]*27))

#dp算法解决找零问题

def dpMakeChange(coinValueList,change,minCoins):
    for cents in range(change+1):
        coinCount = cents
        for j in coinValueList:
            if j <= cents:
                if minCoins[cents - j] + 1 < coinCount:
                    coinCount = minCoins[cents-j] + 1
        minCoins[cents] = coinCount
    return minCoins[change]
#真正实现找零问题，记录所用硬币
def dpMakeChange2(coinValueList,change,minCoins,coinUsed):
    for cents in range(change+1):
        coinCount = cents
        coinUsed[cents] = 1
        for j in coinValueList:
            if j <= cents:
                if minCoins[cents-j] + 1 < coinCount:
                    coinCount = minCoins[cents-j] + 1
                    coinUsed[cents] = j
        minCoins[cents] = coinCount
    return minCoins[change]
def printCoins(coinUsed,change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin
coinVlueList = [1,5,10,21,25]
coinUsed = [0] * 64
minCoins = [0] * 64
dpMakeChange2(coinVlueList,63,minCoins,coinUsed)
printCoins(coinUsed,63)
