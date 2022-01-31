# 6097 : [기초-리스트] 설탕과자 뽑기(py)
h, w = map(int,input().split())
n = int(input())
list = [] # 공백 리스트

for i in range(h+1):
    list.append([]) # 리스트 안에 다른 리스트 추가
    for j in range(w+1):
        list[i].append(0) # 두번째 리스트 안에 0 채워넣기
        
for i in range(n):
    l, d, x, y = map(int,input().split())
    if d==0: # 막대 가로
        for j in range(0,l):
            list[x][y+j]=1
    elif d==1: # 막대 세로
        for j in range(0,l):
            list[x+j][y]=1
            
for i in range(1,h+1):
    for j in range(1,w+1):
        print(list[i][j], end=' ') # 출력
    print() # 줄바꿈