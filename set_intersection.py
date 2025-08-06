#You are given two sets of student roll numbers.
# One set has subscribed to the English newspaper,
# and the other set is subscribed to the French newspaper.
# The same student could be in both sets.
# Your task is to find the total number of students who have subscribed both newspaper.

n=int(input())           #number of students subscribed english np
s1=set(map(int,input().split()))    # student roll numbers seperated with space converted in to set of integers
m=int(input())                      # number of students subscribed French newspaper
s2=set(map(int,input().split()))
s3=s1.intersection(s2)
print(len(s3))
