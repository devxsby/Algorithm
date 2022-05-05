import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    # 두 원의 거리 (원의방정식 활용)
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    if distance == 0: # 두 원이 중심이 같은 경우
        if r1 == r2:
            print(-1) # 두 원의 크기가 같아 겹치는 경우
        else:
            print(0)  # 한 원이 다른 원 안에 들어가 있는 경우
            
    else:             # 두 원의 중심이 다른 경우
        if abs(r1 - r2) == distance or r1 + r2 == distance:
            print(1)  # 내접, 외접일 때
        elif abs(r1 - r2) < distance < (r1 + r2):
            print(2)  # 두 원이 서로다른 두 점에서 만날 때
        else:
            print(0)  # 이외