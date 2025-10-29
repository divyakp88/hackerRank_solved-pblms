import re
def regex(n):
    for _ in range(n):

        try:
            str1 = input()
            re.compile(str1)
            print('True')
        except re.error:
            print('False')


t = int(input())
regex(t)
