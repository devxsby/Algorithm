# 6079 : [기초-종합] 언제까지 더해야 할까?(py)
n = int(input())
sum = 0
for i in range(1,1001):
    sum += i
    if sum >= n:
        break
print(i)