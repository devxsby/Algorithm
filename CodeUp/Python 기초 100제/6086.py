# 6086 : [기초-종합] 거기까지! 이제 그만~(설명)(py)
n = int(input())
sum = 0
cnt = 0
while True:
    sum+=cnt
    cnt+=1
    if sum>=n:
        break
print(sum)