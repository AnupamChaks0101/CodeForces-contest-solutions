#Question --> A. Alarm Clock

import math
t = int(input())
while(t>0):
    a = list(map(float,input().split()))
    if(a[1]>=a[0]):
        print(int(a[1]))
    elif(a[2]-a[3]<=0):
        print("-1")    
    else:
        df = a[2]-a[3]
        if(df==1):
            a[0] = int(a[0])
            a[1] = int(a[1])
            a[2] = int(a[2])
            a[3] = int(a[3])
            ts = ((a[0]-a[1])*a[2])
            ts = int(ts + a[1])
            print(int(ts))
        else:
            a[0] = a[0]-a[1]
            ts = (math.ceil(a[0]/df))*a[2]+a[1]
            print(int(ts))
    t = t-1
