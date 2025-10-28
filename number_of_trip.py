def weightcheck(weight):
    weight.sort()
    trip=0
    i=0
    j=len(weight)-1
    while i<=j:
        if weight[i]+weight[j]<=3.0:

            i=i+1
            j=j-1
        else:
            j=j-1
        trip=trip+1

    return trip
n=int(input())
weight=[]
for i in range(n):
    item=float(input().strip())
    weight.append(item)
result=weightcheck(weight)
print(result)