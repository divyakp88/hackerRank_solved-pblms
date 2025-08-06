
#You have a non-empty set s, and you have to execute N commands
# given in N lines.The commands will be pop, remove and discard.
n=int(input())
s=set(map(int,input().split()))   # split input and map it to integer
op_no=int(input())                #number of operations to be performed
for i in range(op_no):
    parts=input().split()         # accepting the input line to variable parts
    if parts[0]=='pop':
        s.pop()

    elif parts[0]=='remove':
        s.remove(int(parts[1]))

    elif parts[0]=='discard':
        s.discard(int(parts[1]))


sum1=0
for item in s:
    sum1=sum1+item
print(sum1)
