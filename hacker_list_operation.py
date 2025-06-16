N = int(input())
list1 = []
for _ in range(N):
    str1 = input()
    parts = str1.split()

    if parts[0] == 'insert':
        i = int(parts[1])
        item = int(parts[2])
        list1.insert(i, item)

    elif parts[0] == 'append':
        list1.append(int(parts[1]))

    elif parts[0] == 'remove':
        for r in list1:
            if r == int(parts[1]):
                list1.remove(int(parts[1]))
                break
    elif parts[0] == 'pop':
        v = list1.pop()

    elif parts[0] == 'reverse':
        list1.reverse()

    elif parts[0]=='sort':
        list1.sort()

    elif parts[0]=='print':
        print(list1)
