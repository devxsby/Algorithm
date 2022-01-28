# 6082 : [기초-종합] 3 6 9 게임의 왕이 되자(설명)(py)
n = int(input())
for i in range(1,n+1):
    if i%10==3 or i%10==6 or i%10==9:
        print("X", end=' ')
    else:
        print(i, end=' ')