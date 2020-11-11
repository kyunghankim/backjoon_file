A = int(input())
B = int(input())
C = int(input())

num_stringed = str(A*B*C)
for i in range(10):
    print(num_stringed.count(str(i)))
