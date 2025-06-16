
def mutable(str1,index,c):
    l=[]
    l=list(str1)           #changing str in to list
    l[index]=c             #changing character at the specified index
    str1=''.join(l)        #joining the list as a string
    return str1
str=input()             #enter the string
i,char=input().split()    #enter the index and character to be changed, seperated with space
result=mutable(str,int(i),char)
print(result)
