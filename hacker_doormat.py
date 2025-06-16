str=input()                #enter  two numbers, N and M, N is an odd natural number & M is 3 times N
l=str.split()
n=int(l[0])
m=int(l[1])

for i in range(1,(n//2)+1):     # first for loop print Half of the pattern

    stars=2*i-1
    k='.|.'*stars
    print(k.center(m,'-'))
print('WELCOME'.center(m,'-'))
for i in range(n//2,0,-1):       #second for loop print second half of the pattern
    stars=2*i-1
    k = '.|.' * stars
    print(k.center(m, '-'))
