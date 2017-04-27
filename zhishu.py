########«Û÷  ˝
for i in range(1,1000000):
    Nf = 0
    for j in range(2,i-1):
        if i%j == 0:
            Nf = 1
            break
    if Nf == 0:
        print(i)