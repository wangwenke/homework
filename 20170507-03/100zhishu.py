n = 1000000
for n in range(2, x):
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            break
    else:
        print(n)
