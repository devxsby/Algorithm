# 6098 : [기초-리스트] 성실한 개미(py)
list = []
for i in range(10):
    list.append(list(map(int,input().split())))
    
x, y = 1, 1

while True: # 길 찾기
    if (list[x][y] == 0): # 시작 부분 0
        list[x][y] = 9    # 움직이는 곳 9로 채우기
    elif (list[x][y] == 2): # 먹이 발견 시 탐색 종료
        list[x][y] = 9
        break
    
    if (list[x+1][y] == 1 and list[x][y+1] == 1): # 벽 만나면 멈춤
        break
    
    if (list[x][y+1] != 1): # 아래로 이동
        y = y + 1
    elif (list[x+1][y] != 1): # 오른쪽으로 이동
        x = x + 1

for i in range(10): # 출력
    for j in range(10):
        print(list[i][j], end=' ')
    print()