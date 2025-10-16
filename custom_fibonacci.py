
#
# Complete the 'getAutoSaveInterval' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER n as parameter.




def getAutoSaveInterval(n):
    # Write your code here
    fib=[1,2]
    for i in range(2,n+1):
        fib.append(fib[-1]+fib[-2])
    return fib[n]



if __name__ == '__main__':
    n = int(input().strip())

    result = getAutoSaveInterval(n)

    print(result)

