# 6096 : [기초-리스트] 바둑알 십자 뒤집기(py)
''' 출력 error 뜸 다시 풀 것 2022.02.01 '''

list = []

for i in range(19): # 19*19 바둑판 안에 0 채워넣기
    list.append([]) 
    for j in range(19):
        list[i].append(0)
        
for i in range(19):
    list[i] = list(map(int,input().split()))
        
n = int(input())

for i in range(n): # 입력받기
    x, y = map(int,input().split())
    
    for j in range(19):
        if (list[x-1][j] == 0): # 
            list[x-1][j] = 1
        else:
            list[x-1][j] = 0
        
        if (list[j][y-1] == 0): # 
            list[j][y-1] = 1
        else:
            list[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(list[i][j], end=' ') # 출력
    print() # 줄 바꿈