#####쳲���������# 
def feibo(n):
    if n <= 1:
        return n
    else:
         return(feibo(n-1) + feibo(n-2))
number = int(input("��������Ҫ�������������:"))
if number <= 0:
    print("����������")
else:
    print ("����������쳲���������Ϊ:")
for i in range(number):
       print(feibo(i))