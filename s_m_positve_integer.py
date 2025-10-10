
def smallest_integer(list1):
    list1=sorted(set(list1))
    smallest=1
    for num in list1:
        if num==smallest:
            smallest=smallest+1

    return smallest

if __name__=='__main__':
    list1=[]
    n=int(input().strip())
    for _ in range(n):
        item=int(input().strip())
        list1.append(item)
    result=smallest_integer(list1)
    print(result)