NUM = input()
num = int(NUM)

#
for i in range(num):
    #각 자리수 더할 temp지정
    temp = 0
    #str으로 바꾼다음 split후 각 자리수로 더함
    for k in str(i).split():
        a=int(k)
        temp+=a
    if temp+i == num:
        print(i)
        break