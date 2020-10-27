H, M = map(int,input().split())
if M < 45:
    if H ==0:
        print(23,M+15,sep=" ")
    else:
        print(H-1,M+15,sep=" ")
else:
    print(H,M-45,sep=" ")