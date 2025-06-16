def count_sub(str1,sub):
    c=0
    len_sub=len(sub)
    for i in range(len(str1)-len_sub+1):
        if str1[i:i+len_sub]==sub:
            c=c+1
    return c

str1=input().strip()      #Enter the string
sub=input().strip()       #Enter the substring to be counted
count=count_sub(str1,sub)
print(count)