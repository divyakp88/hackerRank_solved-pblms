# Complete the solve function below.

import re
def solve(s):
    parts =re.findall(r'\S+|\s+',s)

    for i in range(len(parts)):
        if (parts[i][0].isalpha() and not parts[i].isspace()):
            parts[i]=parts[i][0].upper()+parts[i][1:]


    return ' '.join(parts)


if __name__ == '__main__':
    fptr = open('my_txt','w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()