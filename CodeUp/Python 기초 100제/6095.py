# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)
n = int(input())
d = [] # 빈 리스트

for i in range(20):
    d.append([]) # 리스트 안에 다른 리스트 추가
    for j in range(20):
        d[i].append(0) # 두번째 리스트 안에 0 채워넣기

for i in range(n):
    x,y = map(int,input().split())
    d[x][y]=1 # 입력 받은 위치 값 1로 변경
    
for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end=' ')
    print() # 줄바꿈