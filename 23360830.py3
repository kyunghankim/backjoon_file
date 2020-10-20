u,d,v = map(int,input().split())

day=(v-d)/(u-d)

print(int(day) if day == int(day) else int(day)+1)
