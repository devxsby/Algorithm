n = int(input())

if n < 100 : # 1~99는 다 한수
    print(n)
else:
    cnt = 0
    for i in range (100, n+1):
        i = list(map(int,str(i)))
        if (i[0]-i[1] == i[1]-i[2]): # 세자리 수 -> 가운데수/ 첫째/셋째수 => 등차수열 비교
            cnt += 1
    print(99+cnt)