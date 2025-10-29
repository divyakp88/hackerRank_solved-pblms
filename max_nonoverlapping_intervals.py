def maximizeNonOverlappingMeetings(meetings):
    # Write your code here
    count = 1
    meetings.sort(key=lambda x: x[1])
    #print(meetings)
    last_end=meetings[0][1]
    for i in range(1,len(meetings)):

        if meetings[i][0]>=last_end:
            count = count + 1
        last_end=meetings[i][1]

    return count


if __name__ == '__main__':
    meetings_rows = int(input().strip())
    meetings_columns = int(input().strip())

    meetings = []

    for _ in range(meetings_rows):
        meetings.append(list(map(int, input().rstrip().split())))

    result = maximizeNonOverlappingMeetings(meetings)

    print(result)
