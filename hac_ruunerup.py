
#Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score.
# You are given  scores. Store them in a list
# and find the score of the runner-up.
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1=list(arr)
    max_val=max(list1)
    runner_up=[item for item in list1 if item!=max_val]
    print(max(runner_up))

