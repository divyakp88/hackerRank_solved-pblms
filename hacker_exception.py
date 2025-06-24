from sys import exception

n = int(input())
for _ in range(n):
    parts = input().split()
    try:
        a = int(parts[0])
        b = int(parts[1])
        print(a/b)
    except ZeroDivisionError as e:
        print('Error code: ',e)
    except ValueError as v:
        print('Error code: ',v)
