t = int(input())
for _ in range(t):
    h, w, n = map(int,input().split()) # 층 수, 방 수, 몇 번째 손님
    num = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(f'{floor*100+num}')