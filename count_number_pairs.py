def countAffordablePairs(prices, budget):
    # Write your code here
    count=0

    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]+prices[j]<=budget:
                count=count+1
    return count
if __name__=='__main__':
    prices_count=int(input().strip())
    prices=[]
    for _ in range(prices_count):
        item=int(input().strip())
        prices.append(item)
    budget=int(input().strip())
    result=countAffordablePairs(prices, budget)
    print(result)