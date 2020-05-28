#Question --> Park Lighting

t = int(input())
while(t>0):
    n,m = input().split()
    tl = 0
    n = int(n)
    m = int(m)
    if((n*m)%2==0):
        print(int(n*m/2))
    else:
        tl = (n*(m-1))/2 + ((n+1)/2)
        print(int(tl))
    t-=1
