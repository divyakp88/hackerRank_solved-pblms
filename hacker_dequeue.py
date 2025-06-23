#A deque is a double-ended queue.
# It can be used to add or remove elements from both ends
#Perform append, pop, popleft and
# appendleft methods on an empty deque d
from collections import deque
d=deque()
n=int(input())
i=1
for _ in range(n):
    parts=input().split()

    if parts[0]=='append':
        d.append(int(parts[1]))

    elif parts[0]=='appendleft':
        d.appendleft(int(parts[1]))

    elif parts[0]=='pop':
        d.pop()

    elif parts[0]=='popleft':
        d.popleft()

for i in d:
    print(i,end=' ')