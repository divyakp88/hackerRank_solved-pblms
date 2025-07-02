# Find the average of n numbers using sets
# print the result float value rounded to 3 decimal places
def average(array):
    sum = 0
    array = set(array)     #convert list to set to avoid duplicate elements
    len1 = len(array)      #calculating the length of the set
    for ele in array:
        sum = sum + ele
    avg = sum / len1
    return format(avg, '.3f')    #average formatted to 3 decimal places

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)