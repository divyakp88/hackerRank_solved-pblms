
def smallest_integer(list1):
    for i in range(n):
        while 1<=list1[i]<=n and list1[i]!=list1[list1[i]-1]:
            list1[i],list1[list1[i]-1]=list1[list1[i]-1],list1[i]

    for i in range(n):
        if list1[i]!=i+1
            return i+1
    return n+1
if __name__=='__main__':
    list1=[]
    n=int(input().strip())
    for _ in range(n):
        item=int(input().strip())
        list1.append(item)
    result=smallest_integer(list1)
    print(result)