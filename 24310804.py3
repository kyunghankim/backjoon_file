from fractions import Fraction

N = int(input())

ring_l = list(map(int,input().split()))

for i in range(1,N):
    ans = Fraction(ring_l[0],1)/Fraction(ring_l[i],1)
    print(ans.numerator,'/',ans.denominator,sep='')
