#求任意整数的几何级数
#number = Sn=a1+a2+a3+……+a(n-1)+an= a1+a1*q+a1*q^2+……+a1*q^(n-2)+a1*q^(n-1)
a= 3;q=2;n=10
sum =0 #引入计数；
for i in range(1, n+1):
    sum += a*(q**i)
print(sum)