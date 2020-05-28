#Question --> B. Honest Coach

t = int(input())
while(t>0):
    n = int(input())
    mn = int(999999999999999999999)
    i = 0
    lst = list(map(int,input().split()))
    lst.sort()
    if(n==2):
        print(abs(lst[0]-lst[1]))
    else:
        for i in range(n-1):
            d = abs(lst[i]-lst[i+1])
            if(d<=mn):
                mn = abs(lst[i]-lst[i+1])
        print(mn)
    t-=1