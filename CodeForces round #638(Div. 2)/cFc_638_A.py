#Question --> A.Phoenix and Balance

t = int(input())
while(t>0):
    n = int(input())
    ts = 0
    ps = 0
    if(n==2):
        print(n)
    else:
        for i in range(1,n+1):
            ts = ts + (2**i)
        m = n/2
        m = int(m)
        for i in range(1,m):
            ps = ps + (2**i)
        ps = ps + (2**n)
        ts = abs((ts-ps)-ps)
        print(ts)
    
    t-=1
