# first letter of each word should begin with a capital letter in a string.
import re
def solve(s):
    parts =re.findall(r'\S+|\s+',s)      #find all words and spaces in string and returns a list
    for i in range(len(parts)):
        if (parts[i][0].isalpha() and not parts[i].isspace()):  # checking first character is a string and not a space
            parts[i]=parts[i][0].upper()+parts[i][1:]           #changing the first char of word to capital letter andjoins it with the remaining parts of the word
    return ''.join(parts)                                       # joining parts list with empty string and returns it


if __name__ == '__main__':
    fptr = open('my_txt','w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()