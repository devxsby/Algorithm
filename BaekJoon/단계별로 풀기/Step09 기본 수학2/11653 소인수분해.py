# 이게 더 빠름
n = int(input())
while n != 1:
    for i in range(2, n + 1):
        if(n % i == 0):
            print(i)
            n = n // i
            break

'''
n = int(input())
i = 2
while n != 1:
    if n % i == 0:
        n = n / i
        print (i)
    else :
        i += 1
'''