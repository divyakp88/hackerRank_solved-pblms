#Given an integer,n , print the following values for each integer i from 1 to n :
#1.Decimal
#2.Octal
#3.Hexadecimal (capitalized)
#4.Binary

def print_formatted(number):
    width=len(format(number,'b'))      #finding the length of largest binary number in the sequence
    for i in range(1,number+1):
        print(str(i).rjust(width),format(i,'o').rjust(width),format(i,'X').rjust(width),format(i,'b').rjust(width))
        #printing decimal,octal,hexa decimal,binary value of number i as right justified within the width...

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
