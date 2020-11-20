N, K = map(int,input().split())
coins_l = []
for i in range(N):
    coins_l.append(int(input()))

used_cnt = 0
coins_l.reverse()
for coin in coins_l:
    if K//coin==0:
        pass
    else:
        used_cnt+= int(K//coin)
        K=(K%coin)
        continue
print(used_cnt)