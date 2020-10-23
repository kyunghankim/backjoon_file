NUM = input()
num = int(NUM)
temp = 0
for i in range(num+1):
    #str으로 바꾼다음 split후 각 자리수로 더함
    digits = list(map(int,str(i)))
    sums = i+sum(digits)
    if sums == num:
        temp = i
        break
print(temp)
        