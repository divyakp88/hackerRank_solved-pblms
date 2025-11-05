def merge(intervals):
    if len(intervals)==1:
        return intervals
    elif len(intervals)==0:
        return []
    else:
        intervals.sort(key=lambda x:x[0])
        merged=[]
        merged.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0]<=merged[-1][1]:
                merged[-1][1]=max(merged[-1][1],intervals[i][1])
            else:
                merged.append(intervals[i])
    return merged



intervals_row=int(input().strip())
intervals_col=int(input().strip())
intervals=[]
for _ in range(intervals_row):
    intervals.append(list(map(int,input().rstrip().split())))
result=merge(intervals)
print('\n'.join([' '.join(map(str,x)) for x in result]))