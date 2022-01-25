# 6077 : [기초-종합] 짝수 합 구하기(설명)(py)
n = int(input())
s = 0
for i in range(1,n+1):
    if i%2!=1:
        s += i
print(s)