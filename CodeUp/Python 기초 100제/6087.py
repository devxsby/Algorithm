# 6087 : [기초-종합] 3의 배수는 통과(설명)(py)
n = int(input())
for i in range (1,n+1):
    if i%3==0:
        continue
    print(i, end=' ')