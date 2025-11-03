def debounceTimestamps(timestamps,K):
    constant=0
    for i in range(1,len(timestamps)):
        if timestamps[i]-timestamps[constant]>=K:
            constant+=1
            timestamps[constant]=timestamps[i]
    return constant+1




if __name__=='__main__':
    timestamps_count=int(input().strip())
    timestamps=[]
    for _ in range(timestamps_count):
        item=int(input().strip())
        timestamps.append(item)
    K=int(input().strip())
    result=debounceTimestamps(timestamps,K)
    print(result)