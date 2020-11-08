A,B = map(int,input().split())
minimum = min((A,B))
list=[]
for i in range(1,minimum+1):
    if A%i==0 and B%i==0: 
        list.append(i)
G = int(list[-1])
L = A*B//G
print(G)
print(L)