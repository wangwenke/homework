#####斐波那契数列# 
def feibo(n):
    if n <= 1:
        return n
    else:
         return(feibo(n-1) + feibo(n-2))
number = int(input("请输入您要输入的任意整数:"))
if number <= 0:
    print("请输入正数")
else:
    print ("所输入数字斐波那契数列为:")
for i in range(number):
       print(feibo(i))