#Question --> B. Maria Breaks the Self-isolation

t = int(input())
while(t>0):
    n = int(input())
    lst = list(map(int,input().split()))
    i = 0
    k = n
    lst.sort()
    for i in range(n-1,-1,-1):
        if(lst[i]<=k):
            print(k+1)
            break
        else:
            k-=1
    if(k==0):
        print(k+1)
    t-=1
