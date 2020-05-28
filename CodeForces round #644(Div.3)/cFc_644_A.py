#Question --> A. Minimal Square

t = int(input())
while(t>0):
    a,b = input().split()
    a = int(a)
    b = int(b)
    s = 0
    
    if(a==b):
        print(4*a*b)
    elif(a==1 or b==1):
        print(a*a*b*b)
    else:
        if(a/b==2):
            print(a*a)
        elif(b/a==2):
            print(b*b)
        else:
            if(a<b):
                a,b=b,a
            if(a>2*b):
                print(a*a)
            else:
                print(4*b*b)
    t-=1
