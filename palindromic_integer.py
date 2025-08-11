#You are given a space separated list of integers. If all the integers are positive,
# then you need to check if any integer is a palindromic integer.
#Condition 1: All the integers in the list should be positive.
#Condition 2: At least one number in the list should be a palindromic integer.
#Then output is True.
#Condition 3:you have to solve this challenge in 3 lines of code or less?
n=int(input())
list1=input().split()
print(all(int(i)>0 for i in list1) and any(i==i[::-1] for i in list1))

